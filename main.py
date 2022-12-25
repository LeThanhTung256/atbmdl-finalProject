import PySimpleGUI as pg

from encrypt.enScreen import encryptScreen
from decrypt.deScreen import decryptScreen
from layout.layout import mainLayout

def main():
    screen = pg.Window('File security', mainLayout, finalize=True, element_justification='center', text_justification='center')
    while True:
        event, values = screen.read()
        if event in {'Exit', pg.WIN_CLOSED}:
            break
        if event == 'Encrypt file':
            en = encryptScreen()
            en.run()
            break
        if event == 'Encrypt file':
            de = decryptScreen()
            de.run()
            break

if __name__ =="__main__":
    main()