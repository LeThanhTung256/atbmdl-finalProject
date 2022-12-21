import random
import hashlib
import json

class FileClass:
  __header = {}
  __id = None
  
  def __init__(self, numOfFile, password=None, fileName=None) -> None:
    # Random số ký tự của chuỗi rác từ 10 đến 20
    self.__header['numOfTrash'] = random.randrange(10, 20)
    self.__header['numOfFile'] = numOfFile

    # Random mảng byte
    ranBytes = random.randbytes(16)

    # Hash(header + byteArray) as id
    self.__id = hashlib.sha256(json.dumps(self.__header).encode('utf-8') + ranBytes)

    # Encode data
    
    print(self.__id.hexdigest())
    print(self.__header)