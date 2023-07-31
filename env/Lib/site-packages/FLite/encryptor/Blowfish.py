from Crypto.Cipher import Blowfish
import base64

class Encryptor(object):
    def __init__(self, key):
        self.key = key.encode('utf-8')

    def encrypt(self, plaintext):
        cipher = Blowfish.new(self.key, Blowfish.MODE_ECB)
        # 在明文前面加上FLite，用于判断解密是否成功
        plaintext = "FLite".encode('utf-8') + plaintext
        plaintext = self.pad(plaintext)
        ciphertext = cipher.encrypt(plaintext)

        return base64.b64encode(ciphertext)

    def decrypt(self, ciphertext):
        cipher = Blowfish.new(self.key, Blowfish.MODE_ECB)
        ciphertext = base64.b64decode(ciphertext)
        plaintext = cipher.decrypt(ciphertext)
        # 判断self.unpad(plaintext)是否以FLite开头
        if plaintext[:5] != "FLite".encode('utf-8'):
            raise Exception("Model decryption Failed maybe!")
        return self.unpad(plaintext[5:])

    # 补齐8的倍数个字符
    def pad(self, s):
        return s + (Blowfish.block_size - len(s) % Blowfish.block_size) * chr(
            Blowfish.block_size - len(s) % Blowfish.block_size).encode('utf-8')

    # 去掉补位字符
    def unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]




