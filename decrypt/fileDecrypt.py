import hashlib
import math

from service import cipherAES, message, messageType, const
from mesScreen import Message

const = const()

class FileDecrypt:
    alive = True
    __header = {}
    __positions = {}

    def __new__(cls, password:str, files:list, filename:str):
        cls.__filename = filename
        # Kiểm tra số lượng file
        if len(files) <= 1:
            message('Files selected amount must bigger than 1!', messageType.FAIL)
            Message('Files selected amount must bigger than 1!', messageType.FAIL)
            cls.alive = False
            return

        # Lấy id, password
        with open(files[0], 'rb') as file:
            data = file.read()
            file.close()
            if len(data) <= 80:
                message('Invalid file!', messageType.FAIL)
                Message('Invalid file!', messageType.FAIL)
                cls.alive = False
                return

            cls.__id = data[:16]
            cls.__header['hashedPass'] = data[16:32]

            # Đọc số lượng file, số lượng trash, số thứ tự
            encryptNums = data[32: 80]
            cipher = cipherAES(cls.__header['hashedPass'], 13)
            try:
                nums = cipher.decrypt(encryptNums)
            except:
                message('Decrypt failed!', messageType.FAIL)
                Message('Decrypt failed!', messageType.FAIL)
                cls.alive = False
                return

            cls.__header['numOfFile'] = int.from_bytes(nums[0:1], 'big')
            cls.__header['numOfTrash'] = int.from_bytes(nums[1:2], 'big')
            fileIndex = int.from_bytes(nums[2:], 'big')
            cls.__positions[fileIndex] = data[80:]
        
        # Kiểm tra password
        hashPass = hashlib.sha1(
            password.encode('utf-8')).hexdigest()[0:16].encode(
                'utf-8')
        if hashPass != cls.__header['hashedPass']:
            message('Wrong password!', messageType.FAIL)
            Message('Wrong password!', messageType.FAIL)
            cls.alive = False
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
                cipher = cipherAES(cls.__header['hashedPass'], 13)
                nums = cipher.decrypt(encryptNums)
                fileIndex = int.from_bytes(nums[2:], 'big')
                cls.__positions[fileIndex] = data[80:]

            # Nếu id, pass khác với cls id pass thì return lỗi
            if id != cls.__id or hashPass != cls.__header['hashedPass']:
                message('Invalid file pieces!', messageType.FAIL)
                Message('Invalid file pieces!', messageType.FAIL)
                cls.alive = False
                return

        # Kiểm tra tính toàn vẹn của dữ liệu
        if len(cls.__positions) != cls.__header['numOfFile']:
            message('Not enough file pieces!', messageType.FAIL)
            Message('Not enough file pieces!', messageType.FAIL)
            cls.alive = False
            return 

        # Ghép data của các file
        tmp = 0
        data = bytes(0)
        for i in sorted(cls.__positions.keys()):
            # Kiểm tra nếu số thứ tự file không hợp lệ
            if i != tmp:
                message('Invalid file pieces!', messageType.FAIL)
                Message('Invalid file pieces!', messageType.FAIL)
                cls.alive = False
                return
        
            data += cls.__positions[i]
            tmp+=1
        
        # Giải mã data
        cipherData = bytes(0)
        lenOfFile = len(data)
        cipher = cipherAES(cls.__header['hashedPass'], cls.__header['numOfTrash'])
        blockSize = 64 + cls.__header['numOfTrash']
        for i in range(math.ceil(lenOfFile / blockSize)):
            if (i + blockSize < lenOfFile):
                text = data[i * blockSize:(i +1) * blockSize]
            else:
                text = data[i * blockSize:]
            cipherData += cipher.decrypt(text)
        
        with open(cls.__filename, 'wb') as file:
            file.write(cipherData)
            file.close()
        message('Decrypt successfully! Decrypted file: ' + cls.__filename, messageType.SUCCESS)
        Message('Decrypt successfully! Decrypted file: ' + cls.__filename, messageType.SUCCESS)
        
