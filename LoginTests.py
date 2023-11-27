import Encrypt

testUser = "test"
testPassword = "ILoveCats2!"

def testLogin():
    print('Running Login tests')
    encrypt = Encrypt.Encrypt()
    encrypt.createAccount(testUser, testPassword)
    accessGranted, usernameExists, username = encrypt.login(testUser, testPassword)
    assert(accessGranted == True)
    assert(usernameExists == True)
    assert(username == testUser)
    print('Passing Login tests\n')

def testWrongPassword():
    print('Running Wrong Password tests')
    encrypt = Encrypt.Encrypt()
    accessGranted, usernameExists, username = encrypt.login('mischa', 'Ilvoecats2!')
    assert(accessGranted == False)
    assert(usernameExists == True)
    assert(username == "mischa")
    print('Passing Wrong Password tests\n')

def testUserNotExist():
    print('Running Username Doesnt Exist tests')
    encrypt = Encrypt.Encrypt()
    accessGranted, usernameExists, username = encrypt.login('nathan', 'Ilvoecats2!')
    assert(accessGranted == False)
    assert(usernameExists == False)
    assert(username == "nathan")
    print('Passing Username Doesnt Exist tests\n')

def removeTestUser(testUser):
    with open("passwd.txt", "r") as file:
        lines = file.readlines()
    file.close()

    file = open("passwd.txt", "r")
    userInFile = ""
    for acc in file:
        userInFile = acc
        acc = acc.split(" ")
        if (acc[0] == testUser):
            break
        else:
            userInFile = ""
    file.close()
    
    with open("passwd.txt", "w") as file:
        for line in lines:
            if (line != userInFile):
                file.write(line)
    file.close()

def runTests():
    print('\n-------------------------')
    print('----- RUNNING TESTS -----')
    print('--------- Login ---------')
    print('-------------------------')
    testLogin()
    testWrongPassword()
    testUserNotExist()
    removeTestUser(testUser)
    print('-------------------------')
    print('----- ALL TESTS PASS ----')
    print('-------------------------')

runTests()