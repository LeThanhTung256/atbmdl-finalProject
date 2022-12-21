from fileEncrypt import FileEncrypt
from service import cipherAES, Positions
import random
import math

# tmp = random.randbytes(40)
# key = random.randbytes(16)
# print(tmp.hex())

# cipher = cipherAES(key, 9)
# en = cipher.encrypt(tmp)
# print(en.hex(), len(en))
# print(cipher.decrypt(en).hex())

filename = 'image.png'
fiEn = FileEncrypt(4, 'adjasldjajdfoejfe', filename)
fiEn.encrypt()









