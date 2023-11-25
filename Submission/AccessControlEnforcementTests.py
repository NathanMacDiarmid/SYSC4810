import ReferenceMonitor
import User
import Encrypt

testUser = "test"
testPassword = "IloveCats2!"

def testEnsureUserHasPermissions():
    print('Running Ensure User Has Permissions tests')
    encrypt = Encrypt.Encrypt()
    monitor = ReferenceMonitor.ReferenceMonitor()
    user = User.User('mischa', testUser, 'Client')
    accessGranted, usernameExists, username = encrypt.login('mischa', testPassword)
    assert(user.getUsername() == username)
    if (accessGranted and usernameExists):
        user.setReadPermissions(monitor.assignReadPermission(user.getRole()))
        user.setWritePermissions(monitor.assignWritePermission(user.getRole()))
    assert(user.getReadPermissions() == ['Account balance', 'Investment portfolio', 'FA contact details'])
    assert(user.getWritePermissions() == [])
    print('Passing Ensure User Has Permissions tests\n')

def testEnsureNewUserHasPermissions():
    print('Running Ensure New User Has Permissions tests')
    encrypt = Encrypt.Encrypt()
    monitor = ReferenceMonitor.ReferenceMonitor()
    user = User.User(testUser, testUser, 'Client')
    encrypt.createAccount(testUser, testPassword)
    accessGranted, usernameExists, username = encrypt.login(testUser, testPassword)
    assert(user.getUsername() == username)
    if (accessGranted and usernameExists):
        user.setReadPermissions(monitor.assignReadPermission(user.getRole()))
        user.setWritePermissions(monitor.assignWritePermission(user.getRole()))
    assert(user.getReadPermissions() == ['Account balance', 'Investment portfolio', 'FA contact details'])
    assert(user.getWritePermissions() == [])
    removeTestUser(testUser)
    print('Passing Ensure New User Has Permissions tests\n')

def testInvalidUserHasNoPermissions():
    print('Running Ensure New User Has No Permissions tests')
    encrypt = Encrypt.Encrypt()
    monitor = ReferenceMonitor.ReferenceMonitor()
    user = User.User(testUser, testUser, 'Client')
    accessGranted, usernameExists, username = encrypt.login(testUser, testPassword)
    assert(testUser == username)
    if (accessGranted and usernameExists):
        user.setReadPermissions(monitor.assignReadPermission(user.getRole()))
        user.setWritePermissions(monitor.assignWritePermission(user.getRole()))
    assert(user.getReadPermissions() == [])
    assert(user.getWritePermissions() == [])
    print('Passing Ensure New User Has No Permissions tests\n')

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
    print('Access Control Enforcement')
    print('-------------------------')
    testEnsureUserHasPermissions()
    testEnsureNewUserHasPermissions()
    testInvalidUserHasNoPermissions()
    print('-------------------------')
    print('----- ALL TESTS PASS ----')
    print('-------------------------')

runTests()