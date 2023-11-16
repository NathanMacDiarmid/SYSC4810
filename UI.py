import Encrypt
class UI:
    def __init__(self) -> None:
        self.encrypt = Encrypt.Encrypt()

    def renderUI(self) -> None:
        print("\nFinvest Holdings")
        print("Client Holdings and Information System")
        print("---------------------------------------")
        username = input("Enter username: ")
        password = input("Enter password: ")
        granted, returningUser = self.encrypt.login(username, password)
        if (granted):
            print("ACCESS GRANTED")
        elif (not returningUser):
            self.renderNewUserUI()
        else:
            print("ACCESS DENIED")
            self.renderUI()
    
    def renderNewUserUI(self) -> None:
        print("\nFinvest Holdings")
        print("Client Holdings and Information System")
        print("CREATE AN ACCOUNT")
        print("---------------------------------------")
        username = input("Enter username: ")
        password = input("Enter password: ")
        if (not self.encrypt.createAccount(username, password)):
            print("INVALID PASSWORD")
            print("Password must include:")
            print("- between 8-12 characters in length")
            print("- one upper case letter")
            print("- one lower case letter")
            print("- one number")
            print("- one special character (!, @, #, $, %, *, ?)")
            print("- not have calendar date pattern")
            print("- not have licence plate pattern")
            print("- not have phone number pattern")
            self.renderNewUserUI()