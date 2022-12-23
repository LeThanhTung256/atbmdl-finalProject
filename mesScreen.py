import PySimpleGUI as pg

from layout.layout import messageLayout
from service import messageType, message

class Message:
    __screen = None

    def __new__(cls, message, type):
        if cls.__screen == None:
            cls.__screen = pg.Window('', messageLayout, finalize=True, element_justification='center')
        if cls.__screen != None:
            cls.__screen.un_hide()
        if type == messageType.FAIL:
            title = 'Error'
            color = 'red'
        if type == messageType.SUCCESS:
            title = 'Success'
            color = 'green'

        cls.__screen.Title = title
        cls.__screen['__TITLE__'].update(title, text_color=color)
        cls.__screen['__MESSAGE__'].update(message, text_color=color)
        cls.__screen['__BUTTON__'].update(button_color = color)

        while True:
            event, values = cls.__screen.read()
            if event in ['Exit', pg.WIN_CLOSED]:
                break

            cls.__screen.hide()
            return
        

        
        