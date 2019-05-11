"""
Encryption class and helper methods.
@author Troy Flagg
"""
from Crypto.Cipher import AES


def pad(s):
    """
    Pads string with \0's, Pilfered this from online.
    :param s: input string to pad.
    :return:
    """
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)


class CryptoMethods:
    """
    This class is used to handle the encryption and decryption of files.
    """
    key = ""
    cipher = ''
    init_vector = ''

    def __init__(self, key, IV):
        """
        Constructor that takes in the AES IV and the AES key.
        :param key: The AES key
        :param IV: The AES IV
        """
        try:
            self.key = key
            self.init_vector = IV.encode()
            self.cipher = AES.new(key, AES.MODE_CBC, self.init_vector)
        except Exception as e:
            print("Key length must be 16, 24 or 32, yours was length: " + str(len(key)))
            print("IV length must be 16, yours was length: ", str(len(IV)))
            raise e

    def encrypt(self, message):
        """
        Pad's text and returns encrypted text, based of a method I found online
        :param message: The Plaintext to encrypt
        :return:
        """
        message = pad(message)
        return self.init_vector + self.cipher.encrypt(message)

    def decrypt(self, ciphertext):
        """
        Decrypts cipher text and strips nonsense \0's, based of a method I found online
        :param ciphertext: The cipher text to decrypt
        :return:
        """
        plaintext = self.cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def encrypt_file(self, file_name):
        """
        Encrypts an entire file to <file_name>.enc, based of a method I found online
        :param file_name: The file to encrypt
        :return:
        """
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext)
        with open(file_name + ".enc", 'wb') as fo:
            fo.write(enc)
        return file_name + '.enc'

    def decrypt_file(self, file_name):
        """
        Decrypts an entire file to <file_name>.decrypt, based of a method I found online
        :param file_name:
        :return:
        """
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext)
        with open(file_name + '.decrypt', 'wb') as fo:
            fo.write(dec)
