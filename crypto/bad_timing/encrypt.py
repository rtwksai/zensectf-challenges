#!usr/bin/python

from secret import flag
from Crypto.Cipher import AES
from hashlib import md5
import time

key = md5(str(int(time.time()))).digest()
padding = 16 - len(flag) % 16
aes = AES.new(key, AES.MODE_ECB)
outData = aes.encrypt(flag + padding* str(padding))
print(outData.encode('base64'))
