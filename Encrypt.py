import hashlib
import random
import PasswordChecker

class Encrypt:
    def __init__(self) -> None:
        self.__filePath = "passwd.txt"
        self.__pswdChecker = PasswordChecker.PasswordChecker()

    def createAccount(self, username, passwd) -> bool:
        if (self.__pswdChecker.checkPswd(username, passwd) and self.checkUsername(username)):
            file = open(self.__filePath, "a")
            salt = str(random.getrandbits(8))
            passwd = salt + passwd
            hashd = hashlib.sha512(passwd.encode())
            file.write(username  + " " + salt + " " + hashd.hexdigest() + "\n")
            file.close()
            return True
        return False

    def login(self, username, passwd) -> bool:
        file = open(self.__filePath, "r")
        usernameExists = False
        for acc in file:
            acc = acc.split(" ")
            acc[2] = acc[2].replace("\n", "")
            if (acc[0] == username):
                usernameExists = True
                passwd = acc[1] + passwd
                hashd = hashlib.sha512(passwd.encode())
                if (hashd.hexdigest() == acc[2]):
                    file.close()
                    return (True, usernameExists, username)
        file.close()
        return (False, usernameExists, "")
    
    def checkUsername(self, username) -> bool:
        file = open(self.__filePath, "r")
        for line in file:
            line = line.split(" ")
            if (line[0] == username):
                return False
        return True