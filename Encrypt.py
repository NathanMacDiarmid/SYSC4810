import hashlib
import random

class Encrypt:
    def __init__(self) -> None:
        pass

    def createAccount(self, username, role, readPermissions, writePermissions, passwd) -> bool:
        if (self.checkPswd(username, passwd)):
            file = open("passwd.txt", "a")
            salt = str(random.getrandbits(8))
            passwd = salt + passwd
            hashd = hashlib.sha512(passwd.encode())
            file.write(username + " " + role + " " + readPermissions + " " + writePermissions + " " + salt + " " + hashd.hexdigest() + "\n")
            file.close()
            return True
        return False

    def login(self, username, passwd) -> bool:
        file = open("passwd.txt", "r")
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
        '''
        Based on examples given from assignment as well as a list of 20 most common passwords by CNBC
        https://www.cnbc.com/2023/11/16/most-common-passwords-70percent-can-be-cracked-in-less-than-a-second.html
        '''
        weakPswd = ["Password1!", "Qwert123!", "Qaz123%wsx", "12345678", "admin123",
                    "123456789", "password", "Aa123456", "1234567890", "UNKNOWN!",
                    "Password", "12345678910", "********"]
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
                    return self.checkForLicencePlate(passwd) and self.checkForCalendar(passwd) and self.checkForPhoneNumber(passwd)
        return False
    
    def checkForLicencePlate(self, passwd) -> bool:
        letterCount = 0
        numberCount = 0
        curr = 0
        prev = 0
        for elem in passwd:
            if (letterCount == 4):
                if (elem.isnumeric()):
                    numberCount += 1
                elif (passwd[curr].isnumeric() and passwd[prev].isnumeric() and numberCount > 0):
                    numberCount += 1
                else:
                    numberCount = 0
            else:
                if (elem.isalpha()):
                    letterCount += 1
                elif (passwd[curr].isalpha() and passwd[prev].isalpha() and letterCount > 0):
                    letterCount += 1
                elif (letterCount != 4):
                    letterCount = 0
            if (letterCount == 4 and numberCount == 3):
                return False
            curr += 1
            prev = curr - 1
        return True
    
    def checkForCalendar(self, passwd) -> bool:
        numberCount = 0
        curr = 0
        prev = 0
        for elem in passwd:
            if (elem.isnumeric()):
                numberCount += 1
            elif (passwd[curr].isnumeric() and passwd[prev].isnumeric() and numberCount > 0):
                numberCount += 1
            elif (numberCount != 6):
                numberCount = 0
            if (numberCount >= 6):
                return False
            curr += 1
            prev = curr - 1
        return True
    
    def checkForPhoneNumber(self, passwd) -> bool:
        numberCount = 0
        curr = 0
        prev = 0
        for elem in passwd:
            if (elem.isnumeric()):
                numberCount += 1
            elif (passwd[curr].isnumeric() and passwd[prev].isnumeric() and numberCount > 0):
                numberCount += 1
            elif (numberCount != 9):
                numberCount = 0
            if (numberCount >= 9):
                return False
            curr += 1
            prev = curr - 1
        return True