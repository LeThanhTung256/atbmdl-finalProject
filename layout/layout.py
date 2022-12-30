import PySimpleGUI as pg

pg.theme('Dark Amber')

mainLayout = [
    [pg.Text('File Security', font='any 30 bold', pad=(None, 50), size=(20, None))],
    [pg.Button('ENCRYPT', font='any 20', pad=((0, 30), 0)), pg.Button('DECRYPT', font='any 20', pad=((30, 0), 0))],
    [pg.Button('Exit', font='any 19', pad=(None, (50, 10)))]
]

encryptLayout = [
    [pg.Text('File Encryption', font='any 30 bold', size=(27, None), pad=(None, 50), justification='center')],
    [pg.FileBrowse('Browse...', (pg.ThisRow, 1), font=('any 19'), size=(9, None), pad=(8, None)), pg.Input(key='__FILE_SELECTED__', font='any 20', size=(32, None))],
    [pg.Text('Password', font='any 20', size=(9, None)), pg.Input(password_char="*", font='any 20', key='__PASSWORD__', size=(32, None))],
    [
        pg.Text('Pieces', font='any 20', size=(9, None)),
        pg.Input(key='__NUM_FILE__', font='any 20', justification='center', size=(4, None)),
        pg.Text(size=(9, None)),
        pg.Checkbox('Delete original file after encryption', key='__IS_DELETE__', font=('any 15'))
    ],
    [pg.Text('', key='__MESSAGE__', font='any 15', pad=(None, 15))],
    [pg.Button('Encrypt', font='any 19', pad=((165, 0), 20), size=(10, None)), pg.Button('Exit', font='any 19', pad=((50, 0), 20), size=(10, None))]
]

decryptLayout = [
    [pg.Text('File Decryption', font='any 30 bold', size=(27, None), pad=(None, 50), justification='center')],
    [pg.FilesBrowse('Browse files...', (pg.ThisRow, 1), font=('any 19'), size=(9, None), pad=(8, None)), pg.Input(key='__FILES_SELECTED__', font='any 20', size=(32, None))],
    [pg.Text('Password', font='any 20', size=(9, None)), pg.Input(password_char="*", font='any 20', key='__PASSWORD__', size=(32, None))],
    [pg.Text('Decrypted file name', font='any 20', size=(9, None)), pg.Input(font='any 20', key='__FILE_NAME__', size=(32, None))],
    [pg.Text('', key='__MESSAGE__', font='any 15', pad=(None, 15))],
    [pg.Button('Decrypt', font='any 19', pad=((165, 0), 20), size=(10, None)), pg.Button('Exit', font='any 19', pad=((50, 0), 20), size=(10, None))]
]

messageLayout = [
    [pg.Text('', key='__TITLE__', pad=(None, 10), font='any 20')],
    [pg.Text('', key='__MESSAGE__', pad=(80, 20), font='any 14')],
    [pg.Text(size=(5, 0)), pg.Button('Exit', key='__BUTTON__', pad=(0, 5))] 
]
