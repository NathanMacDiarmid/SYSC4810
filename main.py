import UI
import User
import ReferenceMonitor

def instantiateUsers() -> list:
    mischa = User.User("mischa", "Mischa Lowery", "Client")
    veronica = User.User("veronica", "Veronica Perez", "Client")

    winston = User.User("winston", "Winston Callahan", "Teller")
    kelan = User.User("kelan", "Kelan Gough", "Teller")

    nelson = User.User("nelson", "Nelson Wilkins", "Financial Advisor")
    kelsie = User.User("kelsie", "Kelsie Chang", "Financial Advisor")

    howard = User.User("howard", "Howard Linkler", "Compliance Officer")
    stefania = User.User("stefania", "Stefania Smart", "Compliance Officer")

    willow = User.User("willow", "Willow Garza", "Premium Client")
    nala = User.User("nala", "Nala Preston", "Premium Client")

    stacy = User.User("stacy", "Stacy Kent", "Investment Analyst")
    keikilana = User.User("keikilana", "Keikilana Kapahu", "Investment Analyst")

    kodi = User.User("kodi", "Kodi Matthews", "Financial Planner")
    malikah = User.User("malikah", "Malikah Wu", "Financial Planner")

    caroline = User.User("caroline", "Caroline Lopez", "Technical Support")
    pawel = User.User("pawel", "Pawel Barclay", "Technical Support")

    return [mischa, veronica, kelan, nelson, howard, stefania, pawel, winston,
            willow, nala, stacy, keikilana, kodi, malikah, caroline, kelsie]

def instantiateCreateAccountUser(newUserID, registeredUsers, monitor) -> list:
    userFound = False
    for i in registeredUsers:
        if (newUserID == i.getUsername()):
            userFound = True
            i.setReadPermissions(monitor.assignReadPermission(i.getRole()))
            i.setWritePermissions(monitor.assignWritePermission(i.getRole()))
    if (not userFound and newUserID != ""):
        newUser = User.User(newUserID, newUserID, "Client")
        registeredUsers.append(newUser)
        newUser.setReadPermissions(monitor.assignReadPermission(newUser.getRole()))
        newUser.setWritePermissions(monitor.assignWritePermission(newUser.getRole()))
    return registeredUsers

def printUserLoggedIn(loggedInUser, registeredUsers) -> None:
    for user in registeredUsers:
        if (loggedInUser == user.getUsername()):
            print("Username (ID): " + user.getUsername())
            print("Role: " + user.getRole())
            if (user.getRole() == "Teller"):
                print("As a Teller, you can only access this account from 9am to 5pm")
            print("\nRead Permissions:")
            if (user.getReadPermissions() == []):
                print("No read permissions")
            else:
                for i in user.getReadPermissions():
                    print(i)
            print("\nWrite Permissions:")
            if (user.getWritePermissions() == []):
                print("No write permissions")
            else:
                for j in user.getWritePermissions():
                    print(j)

def main():
    monitor = ReferenceMonitor.ReferenceMonitor()
    ui = UI.UI()

    registeredUsers = instantiateUsers()

    loggedInUser = ui.renderUI()

    registeredUsers = instantiateCreateAccountUser(loggedInUser, registeredUsers, monitor)

    printUserLoggedIn(loggedInUser, registeredUsers)

main()