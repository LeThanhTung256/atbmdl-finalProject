import PySimpleGUI as pg
import os

from layout import layout
from mesScreen import Message
from service import messageType
from decrypt.fileDecrypt import FileDecrypt

class decryptScreen:
    __screen = None

    def __init__(self) -> None:
        self.__screen = pg.Window('Decrypt file', layout.decryptLayout, element_justification='center', finalize=True)

    def run(self):
        if self.__screen != None:
            self.__screen.un_hide()
        
        while True:
            event, values = self.__screen.read()
            if event in ['Exit', pg.WIN_CLOSED]:
                break
            if event == "Decrypt":
                # Kiểm tra files select
                files = values['__FILES_SELECTED__']
                files = files.split(';')
                flat = False
                for file in files:
                    if file == '':
                        files.remove(file)
                    elif os.path.isfile(file) == False:
                        Message('File {file} không tồn tại'.format(file=file), messageType.FAIL)
                        flat = True
                        break
                if flat == True:
                    continue
            
                if len(files) == 0:
                    Message('Chưa chọn file giải mã'.format(file=file), messageType.FAIL)
                    continue

                # Kiểm tra password
                password = values['__PASSWORD__']
                if password == '':
                    Message('Chưa nhập mật khẩu', messageType.FAIL)
                    continue
                
                # Kiểm tra số lượng file muốn cắt
                fileName = values['__FILE_NAME__']
                if fileName == '':
                    Message('Chưa nhập tên file', messageType.FAIL)
                    continue
    
                # Mã hoá file
                FileDecrypt(password, files, fileName)

        self.__screen.hide()