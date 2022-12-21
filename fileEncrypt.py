import random
import hashlib
import json
import math

from service import cipherAES, Positions
from constant import const

const = const()

class FileEncrypt:
  __header = {}
  
  def __init__(self, numOfFile:int, password:str, fileName:str):
    self.__fileName = fileName
    self.__header['numOfFile'] = numOfFile
    self.__header['hashPass'] = hashlib.sha1(password.encode('utf-8')).hexdigest()[0:16]
    # Random số ký tự của chuỗi rác từ 10 đến 20
    self.__header['numOfTrash'] = random.randrange(10, 20)

    # Random mảng byte
    ranBytes = random.randbytes(16)

    # Hash(header + byteArray) as id
    self.__id = hashlib.sha1(json.dumps(self.__header).encode('utf-8') + ranBytes).digest()

  def encrypt(self):
    # Đọc file ban đầu
    with open(self.__fileName, 'rb') as file:
      data = file.read()
      file.close()

    cipherText = bytes(0)
    lenOfFile = len(data)
    # Mã hoá từng khối
    for i in range(math.ceil(lenOfFile / const.blockSize)):
      if (i + const.blockSize < lenOfFile):
        text = data[i:i + const.blockSize]
      else:
        text = data[i:]
      cipher = cipherAES(self.__header['hashPass'].encode('utf-8'), self.__header['numOfTrash'])
      cipherText += cipher.encrypt(text)

    # Tách giữ liệu ra các file:
    positions = Positions(len(cipherText), self.__header['numOfFile'] - 1).generate()
        
    for i in range(self.__header['numOfFile']):
      # Encrypt(numOfFile + numOfTrash + indexOfFile + 13 byte trash) = 16 bytes
      cipher = cipherAES(self.__header['hashPass'].encode('utf-8'), 13)
      encryptNums = cipher.encrypt(
        self.__header['numOfFile'].to_bytes(1, 'big') +
        self.__header['numOfTrash'].to_bytes(1, 'big') +
        i.to_bytes(1, 'big'))

      # Mỗi file gồm có: id(16 byte) + password(16 byte) + encrypt(numOfFile + numOfTrash + indexOfFile) + encrypt(data)
      dataFile = self.__id + self.__header['hashPass'].encode('utf-8') + encryptNums + data[positions[i]:positions[i+1]]
      fileName = '{fileName}{index}'.format(fileName=self.__fileName, index=i)
      with open(fileName, 'wb') as file:
        file.write(dataFile)
        file.close()
