import PySimpleGUI as pg

from encrypt.enScreen import encryptScreen
from decrypt.deScreen import decryptScreen
from layout.layout import mainLayout

def main():
    screen = pg.Window('FILE SECURITY', mainLayout, finalize=True, element_justification='center', text_justification='center')
    while True:
        event, values = screen.read()
        if event in {'Exit', pg.WIN_CLOSED}:
            break
        if event == 'ENCRYPT':
            en = encryptScreen()
            en.run()
            break
        if event == 'DECRYPT':
            de = decryptScreen()
            de.run()
            break

if __name__ =="__main__":
    main()
