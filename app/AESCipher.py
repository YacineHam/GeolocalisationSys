import base64
import hashlib
#from Crypto import Random
#from Crypto.Cipher import AES

class AESCipher(object):

    def __init__(self, key): 
        #self.bs = AES.block_size
        self.key = hashlib.sha256(key).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = 1#Random.new().read(AES.block_size)
        cipher =1 #AES.new(self.key, AES.MODE_CBC, iv)
        return 1#base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = 1#enc[:AES.block_size]
        cipher = 1#AES.new(self.key, AES.MODE_CBC, iv)
        return 1 # self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]
    