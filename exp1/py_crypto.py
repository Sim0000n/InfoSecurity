from Crypto.Cipher import AES
from binascii import b2a_base64, a2b_base64, b2a_hex, b2a_uu

class Pycrypto(object):
    def __init__(self, key = 'default key'):
        self._mode = AES.MODE_ECB
        self._key = key
    
    def pad(self, x):
        x = bytes(x, encoding='utf8')
        while len(x) % 16 != 0:
            x += b'\0' 
        return x

    def encrypt(self, text): 
        text = self.pad(text)
        aes = AES.new(self.pad(self._key), mode=self._mode)
        encrypt_text = aes.encrypt(text)
        en_str = str(b2a_base64(encrypt_text), encoding='utf-8', errors='ignore')
        return en_str
    
    def decrypt(self, en_text):
        en_text = a2b_base64(en_text)
        aes = AES.new(self.pad(self._key), mode=self._mode)
        de_text = aes.decrypt(en_text)
        return str(de_text, encoding='utf-8', errors='ignore') 
    
    def write_cipher(self, cipher):
        with open('cipher.txt', 'w') as f:
            f.write(cipher)

    def read_cipher(self, path='cipher.txt'):
        with open(path, 'r') as f:
            data = f.read()
        return data
            

if __name__ == '__main__':
    key = 'ilikechinesebest'
    text = 'i am a student,you are a pig'
    en_text = Pycrypto(key).encrypt(text)
    de_text = Pycrypto(key).decrypt(en_text)
    print(en_text)
    print(de_text)
        
        