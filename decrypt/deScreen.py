import PySimpleGUI as pg
import os

from layout import layout
from mesScreen import Message
from service import messageType
from decrypt.fileDecrypt import FileDecrypt

class decryptScreen:
    __screen = None

    def __init__(self) -> None:
        self.__screen = pg.Window('DECRYPTION', layout.decryptLayout, element_justification='left', finalize=True)
        self.__screen.hide()

    def run(self):
        if self.__screen != None:
            self.__screen['__FILES_SELECTED__'].update("")
            self.__screen['__PASSWORD__'].update("")
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
                        Message('File {file} not exist!'.format(file=file), messageType.FAIL)
                        flat = True
                        break
                if flat == True:
                    continue
            
                if len(files) == 0:
                    Message('File pieces not selected!'.format(file=file), messageType.FAIL)
                    continue

                # Kiểm tra password
                password = values['__PASSWORD__']
                if password == '':
                    Message('Password must not be empty!', messageType.FAIL)
                    continue
                
                # Kiểm tra số lượng file muốn cắt
                fileName = values['__FILE_NAME__']
                if fileName == '':
                    Message('File name must not be empty!', messageType.FAIL)
                    continue
    
                # Mã hoá file
                FileDecrypt(password, files, fileName)

        self.__screen.hide()