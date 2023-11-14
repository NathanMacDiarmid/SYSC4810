import hashlib
#text = "hello world"
#hashd = hashlib.sha512(text.encode())

#print(text)
#print(hashd.hexdigest())

class Encrypt:
    def __init__(self) -> None:
        self.text = ""

    def encrypt(self, passwd) -> None:
        file = open("passwd.txt", "a")
        hashd = hashlib.sha512(passwd.encode())
        file.write(hashd.hexdigest() + "\n")
        file.close()

    def decrypt(self) -> None:
        file = open("passwd.txt", "r+")
        print(file.read())
        file.close()
    
crypt = Encrypt()
crypt.encrypt("password123")
crypt.decrypt()