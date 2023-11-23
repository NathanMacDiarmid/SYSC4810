import getpass
import Encrypt
class UI:
    def __init__(self) -> None:
        self.__encrypt = Encrypt.Encrypt()

    def renderUI(self) -> str:
        print("\nFinvest Holdings")
        print("Client Holdings and Information System")
        print("---------------------------------------")
        username = input("Enter username: ")
        password = (getpass.getpass("Enter password: "))
        granted, returningUser, userName = self.__encrypt.login(username, password)
        if (granted):
            print("ACCESS GRANTED")
        elif (not returningUser):
            self.renderNewUserUI()
            userName = ""
        else:
            print("ACCESS DENIED")
            self.renderUI()
        return userName
    
    def renderNewUserUI(self) -> None:
        print("\nFinvest Holdings")
        print("Client Holdings and Information System")
        print("CREATE AN ACCOUNT")
        print("---------------------------------------")
        username = input("Enter username: ")
        password = (getpass.getpass("Enter password: "))
        if (not self.__encrypt.createAccount(username, password)):
            print("INVALID PASSWORD")
            print("Password must include:")
            print("- between 8-12 characters in length")
            print("- one upper case letter")
            print("- one lower case letter")
            print("- one number")
            print("- one special character (!, @, #, $, %, *, ?)")
            print("- not have calendar date pattern")
            print("- not have license plate pattern")
            print("- not have phone number pattern")
            print("USERNAME MUST BE UNIQUE")
            self.renderNewUserUI()