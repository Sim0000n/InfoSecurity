from Crypto.Cipher import AES
from binascii import b2a_base64, a2b_base64, b2a_hex, b2a_uu

class Pycrypto(object):
    def __init__(self, key):
        self._mode = AES.MODE_ECB
        self._key = key
    
    def pad(self, x):
        while len(x) % 16 != 0:
            x += b'\0' 
        return x

    def encrypt(self, text): 
        text = self.pad(text)
        aes = AES.new(self.pad(self._key), mode=self._mode)
        encrypt_text = aes.encrypt(text)
        en_str = str(b2a_base64(encrypt_text), encoding='utf-8', errors='ignore')
        print(type(en_str))
        return en_str
    
    def decrypt(self, en_text):
        en_text = a2b_base64(en_text)
        aes = AES.new(self.pad(self._key), mode=self._mode)
        de_text = aes.decrypt(en_text)
        return str(de_text, encoding='utf-8', errors='ignore') 

if __name__ == '__main__':
    key = b'ilikechinesebest'
    text = b'i am a student,you are a pig'
    en_text = Pycrypto(key).encrypt(text)
    de_text = Pycrypto(key).decrypt(en_text)
    print(en_text)
    print(de_text)
        
        