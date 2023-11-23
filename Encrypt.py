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
        lst = []
        i = 0
        for line in file:
            line = line.split(" ")
            lst.append(line)
            lst[i][2] = lst[i][2].replace("\n", "")
            i += 1
        file.close()
        granted = False
        usernameExists = False
        i = 0
        userIndex = 0
        for acc in lst:
            if (acc[0] == username):
                usernameExists = True
                passwd = acc[1] + passwd
                userIndex = i
                hashd = hashlib.sha512(passwd.encode())
                if (hashd.hexdigest() == acc[2]):
                    granted = True
            i += 1
        return (granted, usernameExists, lst[userIndex][0])
    
    def checkUsername(self, username) -> bool:
        file = open(self.__filePath, "r")
        for line in file:
            line = line.split(" ")
            if (line[0] == username):
                return False
        return True