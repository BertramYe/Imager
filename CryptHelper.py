from settings import crypt_key,crypt_salt


# 在这个里面完全可以定义一个加密方法，用于允许前端用户对图片数据等等的访问和上传

class Crypter():
    def  __init__(self) -> None:
        self.token = crypt_key   # 加密的key
        self.salt = crypt_salt   # 加密盐
        

    def encrypt(self):
        # 加密方法
        
        pass


    def decrypt(self):
        # 解密方法
        
        pass