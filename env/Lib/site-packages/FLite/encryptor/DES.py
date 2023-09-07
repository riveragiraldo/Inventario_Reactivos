from Crypto.Cipher import DES
import base64
"""
这个类中包含了DES加密和解密的基本操作。在创建类实例时需要传入一个8字节长度的密钥（如果密钥长度不足8字节，会使用\x00补足；如果密钥长度超过8字节，会截断为8字节）。然后就可以使用encrypt方法进行加密，使用decrypt方法进行解密了。需要注意的是，加密的明文必须是8字节的整数倍长度，否则会自动使用\x00进行补足。解密时会将补足的\x00去掉。
"""
class Encryptor(object):
    def __init__(self, key):
        self.key = key.encode('utf-8')

    def encrypt(self, plaintext):
        des = DES.new(self.key, DES.MODE_ECB)
        # 在明文前面加上FLite，用于判断解密是否成功
        plaintext = "FLite".encode('utf-8') + plaintext
        plaintext = self.pad(plaintext)
        ciphertext = des.encrypt(plaintext)

        return base64.b64encode(ciphertext)

    def decrypt(self, ciphertext):
        des = DES.new(self.key, DES.MODE_ECB)
        ciphertext = base64.b64decode(ciphertext)
        plaintext = des.decrypt(ciphertext)
        #判断self.unpad(plaintext)是否以FLite开头
        if plaintext[:5] != "FLite".encode('utf-8'):
            raise Exception("Model decryption Failed maybe!")
        return self.unpad(plaintext[5:])


    # 补齐8的倍数个字符
    def pad(self, s):
        return s + (DES.block_size - len(s) % DES.block_size) * chr(
            DES.block_size - len(s) % DES.block_size).encode('utf-8')

    # 去掉补位字符
    def unpad(self, s):
        return s[:-ord(s[len(s) - 1:])]

