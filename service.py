from Crypto.Cipher import AES
from random import randbytes, randint, choice
import string
import os
from enum import Enum

# Mã hoá khối data
class cipherAES:
  def __init__(self, key: bytes, numOfTrash: int):
    self.__key = key
    self.__numOfTrash = numOfTrash
    
  # Hàm mã hoá một khối data
  def encrypt(self, blockData: bytes):
    # Tạo một cipher với key và mode EAX 
    cipher = AES.new(self.__key, AES.MODE_EAX)

    # Mã hoá block data
    cipherText, tag = cipher.encrypt_and_digest(blockData)

    # Return một chuỗi bytes gồm: nonce(16 bytes) + tag(16 bytes) + cipherText + trash
    trash = randbytes(self.__numOfTrash)
    return cipher.nonce + tag + cipherText + trash

  # Hàm giải mã một khối data
  def decrypt(self, blockData: bytes):
    # Tách các thành phần của block
    nonce = blockData[0:16]
    tag = blockData[16:32]
    data = blockData[32:len(blockData)-self.__numOfTrash]

    # Tạo lại cipher đã mã hoá block này
    cipher = AES.new(self.__key, AES.MODE_EAX, nonce)

    # Giải mã block
    return cipher.decrypt_and_verify(data, tag)

# Tạo một list position cho việc cắt file
class Node:
    def __init__(self, start: int, end: int):
      self.__start = start
      self.__end = end
      self.__sub = end - start
    
    def get(self, property:str = None):
      value = {
        'start': self.__start,
        'end': self.__end,
        'sub': self.__sub,
      }
      if property == None:
        return value
      else:
        return value[property]

class Positions:
  def __new__(cls, maxPosition: int, numberOfPos):
    cls.__listPos = [0, maxPosition]
    cls.__listNode = [Node(0, maxPosition)]
    for i in range(numberOfPos):
      # Tìm khoảng lớn nhất để lấy random
      maxSubIndex = 0
      maxSub = cls.__listNode[maxSubIndex].get('sub')
      numberOfListNode = len(cls.__listNode)
      if numberOfListNode > 1:
        for nodeIndex in range(numberOfListNode):
          sub = cls.__listNode[nodeIndex].get('sub')
          if sub > maxSub:
            maxSub = sub
            maxSubIndex = nodeIndex
      
      # Random một số
      node = cls.__listNode[maxSubIndex]
      pos = randint(node.get('start') + 1, node.get('end') - 1)

      # Thêm poi vào list
      cls.__listPos.append(pos)

      # Thay đổi list Node
      cls.__listNode.extend([Node(node.get('start'), pos), Node(pos, node.get('end'))])
      del cls.__listNode[maxSubIndex]

    return sorted(cls.__listPos)

# Tạo ra một chuỗi string ngẫu nhiên
class RandomString:
  def __new__(cls, length:int):
    letters = string.ascii_lowercase + string.digits
    text = ''.join(choice(letters) for i in range(length))
    return text
  
# Tạo ra một forder ẩn để lưu file cut
class HidenFolder:
  def __new__(cls, length):
    folder = '.' + RandomString(length)
    while os.path.isdir(folder):
      folder = '.' + RandomString(length)
    
    os.mkdir(folder)
    return folder

class messageType(Enum):
    SUCCESS = 0
    FAIL = 1

class message:
    __text:str = ''
    __type:messageType

    def __init__(self, text:str, type:messageType):
        self.__text = text
        self.__type = type

        if self.__type == messageType.SUCCESS:
            print('SUCCESS: ' + self.__text)
        elif self.__type == messageType.FAIL:
            print('FAIL: ' + self.__text)

def constant(f):
    def fset(self, value):
        raise TypeError
    def fget(self):
        return f()
    return property(fget, fset)

class const(object):
    @constant
    def blockSize():
        return 32
      