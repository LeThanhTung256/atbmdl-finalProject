from enum import Enum

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
