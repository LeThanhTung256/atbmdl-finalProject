import random
import hashlib
import math

from service import cipherAES
from constant import const
from message import message, messageType

const = const()

class FileDecrypt:
    alive = True
    __header = {}
    __positions = {}

    def __init__(self,password:str, files:list, filename:str):
        self.__filename = filename
        # Kiểm tra số lượng file
        if len(files) <= 1:
            message('Số lượng file phải lớn hơn 1', messageType.FAIL)
            self.alive = False
            return

        # Lấy id, password
        with open(files[0], 'rb') as file:
            data = file.read()
            file.close()
            self.__id = data[:16]
            self.__header['hassPass'] = data[16:32]

            # Đọc số lượng file, số lượng trash, số thứ tự
            encryptNums = data[32: 80]
            cipher = cipherAES(self.__header['hassPass'], 13)
            nums = cipher.decrypt(encryptNums)
            self.__header['numOfFile'] = int.from_bytes(nums[0:1], 'big')
            self.__header['numOfTrash'] = int.from_bytes(nums[1:2], 'big')
            fileIndex = int.from_bytes(nums[2:], 'big')
            self.__positions[fileIndex] = data[80:]
        
        # Kiểm tra password
        hashPass = hashlib.sha1(
            password.encode('utf-8')).hexdigest()[0:16].encode(
                'utf-8')
        if hashPass != self.__header['hassPass']:
            message('Mật khẩu sai', messageType.FAIL)
            print(self.__header['hassPass'], '\n', hashPass)
            self.alive = False
            return
            
        # So sánh id của các file
        for i in range(1, len(files)):
            # Lấy id của từng file
            with open(files[i], 'rb') as file:
                data = file.read()
                file.close()
                id = data[:16]
                hashPass = data[16:32]
                encryptNums = data[32: 80]
                cipher = cipherAES(self.__header['hassPass'], 13)
                nums = cipher.decrypt(encryptNums)
                fileIndex = int.from_bytes(nums[2:], 'big')
                self.__positions[fileIndex] = data[80:]

            # Nếu id, pass khác với self id pass thì return lỗi
            if id != self.__id or hashPass != self.__header['hassPass']:
                message('Danh sách file không phù hợp', messageType.FAIL)
                self.alive = False
                return

    def run(self):
        # Kiểm tra tính toàn vẹn của dữ liệu
        if len(self.__positions) != self.__header['numOfFile']:
            message('Danh sách file không hợp lệ: Số lượng file không đúng', messageType.FAIL)
            self.alive = False
            return 

        # Ghép data của các file
        tmp = 0
        data = bytes(0)
        for i in sorted(self.__positions.keys()):
            # Kiểm tra nếu số thứ tự file không hợp lệ
            if i != tmp:
                message('Danh sách file không hợp lệ', messageType.FAIL)
                self.alive = False
                return
        
            data += self.__positions[i]
            tmp+=1
        
        # Giải mã data
        cipherData = bytes(0)
        lenOfFile = len(data)
        cipher = cipherAES(self.__header['hassPass'], self.__header['numOfTrash'])
        blockSize = 64 + self.__header['numOfTrash']
        for i in range(math.ceil(lenOfFile / blockSize)):
            if (i + blockSize < lenOfFile):
                text = data[i * blockSize:(i +1) * blockSize]
            else:
                text = data[i * blockSize:]
            cipherData += cipher.decrypt(text)
        
        with open(self.__filename, 'wb') as file:
            file.write(cipherData)
            file.close()
        message('Giải mã thành công. File giải mã: ' + self.__filename, messageType.SUCCESS)
        
