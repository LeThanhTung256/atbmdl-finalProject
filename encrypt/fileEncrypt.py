import random
import hashlib
import json
import math
import os

from service import cipherAES, Positions, RandomString, HiddenFolder, message, messageType, const
from mesScreen import Message
const = const()

class FileEncrypt:
    __header = {}

    def __new__(cls, numOfFile: int, password: str, fileName: str, deleteFile:bool):
        cls.__fileName = fileName
        cls.__header['numOfFile'] = numOfFile
        cls.__header['hashPass'] = hashlib.sha1(
            password.encode('utf-8')).hexdigest()[0:16]
        # Random số ký tự của chuỗi rác từ 10 đến 20
        cls.__header['numOfTrash'] = random.randrange(10, 20)

        # Random mảng byte
        ranBytes = random.randbytes(16)

        # Hash(header + byteArray) as id
        cls.__id = hashlib.sha1(json.dumps(cls.__header).encode(
            'utf-8') + ranBytes).digest()[0:16]

        # Đọc file ban đầu
        with open(cls.__fileName, 'rb') as file:
            data = file.read()
            file.close()

        cipherText = bytes(0)
        lenOfFile = len(data)
        cipher = cipherAES(cls.__header['hashPass'].encode(
                'utf-8'), cls.__header['numOfTrash'])
        # Mã hoá từng khối
        for i in range(math.ceil(lenOfFile / const.blockSize)):
            if (i + const.blockSize < lenOfFile):
                text = data[i * const.blockSize:(i + 1) * const.blockSize]
            else:
                text = data[i * const.blockSize:]
            cipherText += cipher.encrypt(text)

        # Tách giữ liệu ra các file:
        positions = Positions(
            len(cipherText), cls.__header['numOfFile'] - 1)

        # Tạo một hidden forder
        folder = HiddenFolder(8)

        for i in range(cls.__header['numOfFile']):
            # Encrypt(numOfFile + numOfTrash + indexOfFile + 13 byte trash) = 16 bytes
            cipher = cipherAES(cls.__header['hashPass'].encode('utf-8'), 13)
            encryptNums = cipher.encrypt(
                cls.__header['numOfFile'].to_bytes(1, 'big') +
                cls.__header['numOfTrash'].to_bytes(1, 'big') +
                i.to_bytes(1, 'big'))

            # Mỗi file gồm có: id(16 byte) + password(16 byte) + encrypt(numOfFile + numOfTrash + indexOfFile)(48 bytes) + encrypt(data)
            dataFile = cls.__id + cls.__header['hashPass'].encode(
                'utf-8') + encryptNums + cipherText[positions[i]:positions[i+1]]

            # Tạo ngẫu nhiên tên file gồm 6 ký tự
            fileName = folder + '/.' + RandomString(6)
            with open(fileName + 'txt', 'wb') as file:
                file.write(dataFile)
                file.close()
            
        # Xoá file ban đầu
        if deleteFile == True:
            os.remove(cls.__fileName)
        
        message('Mã hoá file thành công', messageType.SUCCESS)
        Message('Mã hoá file thành công', messageType.SUCCESS)
        
