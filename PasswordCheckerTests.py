import PasswordChecker

def testUsernameEqPassword():
    print('Running Username Equals Password tests')
    checker = PasswordChecker.PasswordChecker()
    assert(checker.checkPswd("username", "username") == False)
    print('Passing Username Equals Password tests\n')

def testPasswordOnList():
    print('Running Password on Blacklist tests')
    checker = PasswordChecker.PasswordChecker()
    assert(checker.checkPswd("username", "Password1!") == False)
    print('Passing Password on Blacklist tests\n')

def testNoPassword():
    print('Running Password too Short tests')
    checker = PasswordChecker.PasswordChecker()
    assert(checker.checkPswd("username", "") == False)
    print('Passing Password too Short tests\n')

def testPasswordTooShort():
    print('Running Password too Short tests')
    checker = PasswordChecker.PasswordChecker()
    assert(checker.checkPswd("username", "Pas1!") == False)
    print('Passing Password too Short tests\n')

def testPasswordTooLong():
    print('Running Password too Long tests')
    checker = PasswordChecker.PasswordChecker()
    assert(checker.checkPswd("username", "Passsssssssssssss1!") == False)
    print('Passing Password too Long tests\n')

def testPasswordNoUpper():
    print('Running Password No Upper Case tests')
    checker = PasswordChecker.PasswordChecker()
    assert(checker.checkPswd("username", "ilovecats2!") == False)
    print('Passing Password No Upper Case tests\n')

def testPasswordNoLower():
    print('Running Password No Lower Case tests')
    checker = PasswordChecker.PasswordChecker()
    assert(checker.checkPswd("username", "ILOVECATS2!") == False)
    print('Passing Password No Lower Case tests\n')

def testPasswordNoNumber():
    print('Running Password No Number tests')
    checker = PasswordChecker.PasswordChecker()
    assert(checker.checkPswd("username", "IloveCats!") == False)
    print('Passing Password No Number tests\n')

def testPasswordNoSpecialChar():
    print('Running Password No Special Character tests')
    checker = PasswordChecker.PasswordChecker()
    assert(checker.checkPswd("username", "IloveCats!") == False)
    print('Passing Password No Special Character tests\n')

def testPasswordSpecialCharNotInList():
    print('Running Password No Special Character from List tests')
    checker = PasswordChecker.PasswordChecker()
    assert(checker.checkPswd("username", "IloveCats2&") == False)
    print('Passing Password No Special Character from List tests\n')

def testPasswordForLicensePlateBeg():
    print('Running Password Contains License Plate at Beginning tests')
    checker = PasswordChecker.PasswordChecker()
    assert(checker.checkPswd("username", "Abcd123$l") == False)
    print('Passing Password Contains License Plate at Beginning tests\n')

def testPasswordForLicensePlateMid():
    print('Running Password Contains License Plate at Middle tests')
    checker = PasswordChecker.PasswordChecker()
    assert(checker.checkPswd("username", "45Acde423!") == False)
    print('Passing Password Contains License Plate at Middle tests\n')

def testPasswordForLicensePlateEnd():
    print('Running Password Contains License Plate at End tests')
    checker = PasswordChecker.PasswordChecker()
    assert(checker.checkPswd("username", "45!Acbd123") == False)
    print('Passing Password Contains License Plate at End tests\n')

def testPasswordForCalendar():
    print('Running Password Contains License Plate at End tests')
    checker = PasswordChecker.PasswordChecker()
    assert(checker.checkPswd("username", "123456789") == False)
    print('Passing Password Contains License Plate at End tests\n')

def testPasswordValid():
    print('Running Password Contains License Plate at End tests')
    checker = PasswordChecker.PasswordChecker()
    assert(checker.checkPswd("username", "IloveCats2!") == True)
    print('Passing Password Contains License Plate at End tests\n')

def runTests():
    print('\n-------------------------')
    print('----- RUNNING TESTS -----')
    print('---- Password Checker ---')
    print('-------------------------')
    testUsernameEqPassword()
    testPasswordOnList()
    testNoPassword()
    testPasswordTooShort()
    testPasswordTooLong()
    testPasswordNoUpper()
    testPasswordNoLower()
    testPasswordNoNumber()
    testPasswordNoSpecialChar()
    testPasswordSpecialCharNotInList()
    testPasswordForLicensePlateBeg()
    testPasswordForLicensePlateMid()
    testPasswordForLicensePlateEnd()
    testPasswordForCalendar()
    testPasswordValid()
    print('-------------------------')
    print('----- ALL TESTS PASS ----')
    print('-------------------------')

runTests()