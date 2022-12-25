import PySimpleGUI as pg

pg.theme('DarkGrey4')

encryptLayout = [
    [pg.Text('Mã hoá file', font='any 30 bold', pad=(None, 50))],
    [pg.FileBrowse('Select file', (pg.ThisRow, 1), font=('any 17')), pg.Input(key='__FILE_SELECTED__', font='any 19', size=(32, 0))],
    [pg.Text('Mật khẩu', font='any 20'), pg.Input(password_char="*", font='any 19', key='__PASSWORD__', size=(32, 0))],
    [pg.Text('Số lượng file cắt', font=('any 20')), pg.Input(key='__NUM_FILE__', font='any 19', justification='center', size=(4, None)),
    pg.T(size=(5, 0)), pg.Checkbox('Xoá file sau khi mã hoá', key='__IS_DELETE__', font=('any 20'))],
    [pg.Text('', key='__MESSAGE__', font='any 15', pad=(None, 15))],
    [pg.Button('Encrypt', font='any 19', pad=(None, 20), size=(10, 0)), pg.Button('Exit', font='any 19', size=(10, 0))]
]

decryptLayout = [
    [pg.Text('Giải mã file', font='any 30 bold', pad=(None, 50))],
    [pg.FilesBrowse('Select files', (pg.ThisRow, 1), font=('any 17'), size=(11, 0)), pg.Input(key='__FILES_SELECTED__', font='any 19', size=(32, 0))],
    [pg.Text('Mật khẩu', font='any 20', size=(10, 0)), pg.Input(password_char="*", font='any 19', key='__PASSWORD__', size=(32, 0))],
    [pg.Text('Tên file', font='any 20', size=(10, 0)), pg.Input(font='any 19', key='__FILE_NAME__', size=(32, 0))],
    [pg.Text('', key='__MESSAGE__', font='any 15', pad=(None, 15))],
    [pg.Button('Decrypt', font='any 19', pad=(None, 20), size=(10, 0)), pg.Button('Exit', font='any 19', size=(10, 0))]
]

messageLayout = [
    [pg.Text('', key='__TITLE__', pad=(None, 10), font='any 20')],
    [pg.Text('', key='__MESSAGE__', pad=(80, 20), font='any 14')],
    [pg.Text(size=(5, 0)), pg.Button('Exit', key='__BUTTON__', pad=(0, 5))] 
]

mainLayout = [
    [pg.Text('File security', font='any 30 bold', pad=(None, 50), size=(20, None))],
    [pg.Button('Encrypt file', font='any 20'), pg.Button('Decrypt file', font='any 20')],
    [pg.T(size=(30, 0), pad=(None, 50)), pg.Button('Exit', font='any 19')]
]