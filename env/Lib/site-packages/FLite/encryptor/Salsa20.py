from Crypto.Cipher import Salsa20
import base64

class Encryptor(object):
    def __init__(self, key):
        self.key = key.encode('utf-8')

    def encrypt(self, plaintext):
        cipher = Salsa20.new(self.key)
        plaintext = b"FLite" + plaintext
        ciphertext = cipher.nonce + cipher.encrypt(self.pad(plaintext))
        return base64.b64encode(ciphertext)

    def decrypt(self, ciphertext):
        ciphertext = base64.b64decode(ciphertext)
        nonce = ciphertext[:8]
        cipher = Salsa20.new(self.key, nonce=nonce)
        plaintext = cipher.decrypt(ciphertext[8:])
        if plaintext[:5] != b"FLite":
            raise Exception("Model decryption Failed maybe!")
        return self.unpad(plaintext[5:])

    # 补齐16的倍数个字符
    def pad(self, s):
        padding_length = Salsa20.block_size - len(s) % Salsa20.block_size
        padding = bytes([padding_length] * padding_length)
        return s + padding

    # 去掉补位字符
    def unpad(self, s):
        padding_length = s[-1]
        return s[:-padding_length]
