import PySimpleGUI as pg
import os

from layout import layout
from mesScreen import Message
from service import messageType
from encrypt.fileEncrypt import FileEncrypt

class encryptScreen:
    __screen = None

    def __init__(self) -> None:
        self.__screen = pg.Window('Encrypt file', layout.encryptLayout, element_justification='left', finalize=True)

    def run(self):
        if self.__screen != None:
            self.__screen.un_hide()
        
        while True:
            event, values = self.__screen.read()
            if event == 'Exit' or event == pg.WIN_CLOSED:
                break
            if event == "Encrypt":
                # Kiểm tra file select
                fileName = values['__FILE_SELECTED__']
                if fileName == '':
                    Message('Chưa chọn file mã hoá', messageType.FAIL)
                    continue
                elif os.path.isfile(fileName) == False:
                    Message('File không tồn tại', messageType.FAIL)
                    continue

                # Kiểm tra password
                password = values['__PASSWORD__']
                if password == '':
                    Message('Chưa nhập mật khẩu', messageType.FAIL)
                    continue
                
                # Kiểm tra số lượng file muốn cắt
                numOfFiles = values['__NUM_FILE__']
                if numOfFiles == '':
                    numOfFiles == 2
                    self.__screen['__NUM_FILE__'].update(2)
                else:
                    try:
                        numOfFiles = int(numOfFiles)
                        if numOfFiles <= 1:
                            Message('Số lượng file phải là số tự nhiên lớn hơn 1', messageType.FAIL)
                            continue
                    except:
                        Message('Số lượng file phải là số tự nhiên lớn hơn 1', messageType.FAIL)
                        continue
                
                # Mã hoá file
                isDelete = values['__IS_DELETE__']
                FileEncrypt(numOfFiles, password, fileName, isDelete)

        self.__screen.close()