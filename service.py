from Crypto.Cipher import AES
from random import randbytes, randint
import time

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

    # Return một chuỗi (64 + numOfTrash) bytes gồm: nonce(16 bytes) + tag(16 bytes) + cipherText(32 bytes) + trash
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
  def __init__(self, maxPosition: int, numberOfPos):
    self.__listPos = [0, maxPosition]
    self.__listNode = [Node(0, maxPosition)]
    for i in range(numberOfPos):
      # Tìm khoảng lớn nhất để lấy random
      maxSubIndex = 0
      maxSub = self.__listNode[maxSubIndex].get('sub')
      numberOfListNode = len(self.__listNode)
      if numberOfListNode > 1:
        for nodeIndex in range(numberOfListNode):
          sub = self.__listNode[nodeIndex].get('sub')
          if sub > maxSub:
            maxSub = sub
            maxSubIndex = nodeIndex
      
      # Random một số
      node = self.__listNode[maxSubIndex]
      pos = randint(node.get('start') + 1, node.get('end') - 1)

      # Thêm poi vào list
      self.__listPos.append(pos)

      # Thay đổi list Node
      self.__listNode.extend([Node(node.get('start'), pos), Node(pos, node.get('end'))])
      del self.__listNode[maxSubIndex]

  def generate(self):
    return sorted(self.__listPos)
      