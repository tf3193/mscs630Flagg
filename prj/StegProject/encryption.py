from Crypto.Cipher import AES

validKeyLength = [16, 24, 32]

class CryptoMethods:
    key = ""
    cipher = ''
    decipher = ''

    def __init__(self, key):
        if key.len() in validKeyLength:
            self.key = key
            self.cipher = AES.new(key, AES.MODE_ECB)
            self.decipher = AES.new(key, AES.MODE_ECB)
        else:
            print("Key lengths must be 16, 24 or 32")
            return 0

    def encryptText(self, text):
        return cipher.encrypt(text)

    def decrypyText(self, text):
        return decipher.decrypy(text)
