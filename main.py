from fileEncrypt import FileEncrypt
from fileDecrypt import FileDecrypt
from service import cipherAES, Positions
import random
import math
import os


# filename = 'image.jpg'
# fiEn = FileEncrypt(4, 'adjasldjajdfoejfe', filename)
# fiEn.run()

folder = '.d54co9dg'
files = ['.314tu7txt', '.mgi9f0txt', '.pgwx9stxt', '.pih3i8txt']
for i in range(len(files)):
    files[i] = folder + '/' + files[i]
file = FileDecrypt('adjasldjajdfoejfe', files, 'decr.jpg')
file.run()


        








