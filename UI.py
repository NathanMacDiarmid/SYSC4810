def renderUI():
    print("\nFinvest Holdings")
    print("Client Holdings and Information System")
    print("---------------------------------------")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if (username == "nathan" and password == "123"):
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")