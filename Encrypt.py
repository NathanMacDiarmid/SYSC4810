import hashlib
import random

class Encrypt:
    def __init__(self) -> None:
        pass

    def createAccount(self, username, passwd) -> bool:
        if (self.checkPswd(username, passwd)):
            file = open("\Documents\School\SYSC4810\passwd.txt", "a")
            salt = str(random.getrandbits(8))
            passwd = salt + passwd
            hashd = hashlib.sha512(passwd.encode())
            file.write(username + " " + salt + " " + hashd.hexdigest() + "\n")
            file.close()
            return True
        return False

    def login(self, username, passwd) -> bool:
        file = open("\Documents\School\SYSC4810\passwd.txt", "r")
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
        for acc in lst:
            if (acc[0] == username):
                usernameExists = True
                passwd = acc[1] + passwd
                hashd = hashlib.sha512(passwd.encode())
                if (hashd.hexdigest() == acc[2]):
                    granted = True
        return (granted, usernameExists)
    
    def checkPswd(self, username, passwd) -> bool:
        weakPswd = ["Password1!", "Qwert123!", "Qaz123%wsx"]
        for wp in weakPswd:
            if (passwd == wp):
                return False
        if (passwd == username):
            return False
        elif (len(passwd) >= 8 and len(passwd) <= 12):
            isUpper = False
            isLower = False
            isDigit = False
            containsSpecChar = False
            specialChar = ["!", "@", "#", "$", "%", "?", "*"]
            for elem in passwd:
                if (elem.isupper()):
                    isUpper = True
                elif (elem.islower()):
                    isLower = True
                elif (elem.isnumeric()):
                    isDigit = True
                for i in specialChar:
                    if (elem == i):
                        containsSpecChar = True
                if (isUpper and isLower and isDigit and containsSpecChar):
                    return True
        return False