import Encrypt

testUser = "test"
testPassword = "ILoveCats2!"

def testEnrolNewUser():
    print('Running Enroll New User tests')
    encrypt = Encrypt.Encrypt()
    assert(encrypt.createAccount(testUser, testPassword) == True)
    print('Passing Enroll New User tests\n')

def testEnrolExistingUser():
    print('Running Enroll New User Exists tests')
    encrypt = Encrypt.Encrypt()
    assert(encrypt.createAccount(testUser, testPassword) == False)
    print('Passing Enroll New User Exists tests\n')

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
    print('------- Enrolment -------')
    print('-------------------------')
    testEnrolNewUser()
    testEnrolExistingUser()
    removeTestUser(testUser)
    print('-------------------------')
    print('----- ALL TESTS PASS ----')
    print('-------------------------')

runTests()