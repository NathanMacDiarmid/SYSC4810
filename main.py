import UI
import User
import ReferenceMonitor

def main():
    monitor = ReferenceMonitor.ReferenceMonitor()
    ui = UI.UI()
    loggedInUser = ui.renderUI()

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

    registeredUsers = [mischa, veronica, kelan, nelson, howard, stefania, pawel,
                       willow, nala, stacy, keikilana, kodi, malikah, caroline]
    
    userFound = False
    for i in registeredUsers:
        if (loggedInUser == i.getUsername()):
            userFound = True
    if (not userFound and loggedInUser != ""):
        newUser = User.User(loggedInUser, loggedInUser, "Client")
        registeredUsers.append(newUser)
        newUser.setReadPermissions(monitor.assignReadPermission(newUser.getRole()))
        newUser.setWritePermissions(monitor.assignWritePermission(newUser.getRole()))

    # Assign Read Permission

    mischa.setReadPermissions(monitor.assignReadPermission(mischa.getRole()))
    veronica.setReadPermissions(monitor.assignReadPermission(veronica.getRole()))

    winston.setReadPermissions(monitor.assignReadPermission(winston.getRole()))
    kelan.setReadPermissions(monitor.assignReadPermission(kelan.getRole()))

    nelson.setReadPermissions(monitor.assignReadPermission(nelson.getRole()))
    kelsie.setReadPermissions(monitor.assignReadPermission(kelsie.getRole()))

    howard.setReadPermissions(monitor.assignReadPermission(howard.getRole()))
    stefania.setReadPermissions(monitor.assignReadPermission(stefania.getRole()))

    willow.setReadPermissions(monitor.assignReadPermission(willow.getRole()))
    nala.setReadPermissions(monitor.assignReadPermission(nala.getRole()))

    stacy.setReadPermissions(monitor.assignReadPermission(stacy.getRole()))
    keikilana.setReadPermissions(monitor.assignReadPermission(keikilana.getRole()))

    kodi.setReadPermissions(monitor.assignReadPermission(kodi.getRole()))
    malikah.setReadPermissions(monitor.assignReadPermission(malikah.getRole()))

    caroline.setReadPermissions(monitor.assignReadPermission(caroline.getRole()))
    pawel.setReadPermissions(monitor.assignReadPermission(pawel.getRole()))

    # Assign Write Permission

    mischa.setWritePermissions(monitor.assignWritePermission(mischa.getRole()))
    veronica.setWritePermissions(monitor.assignWritePermission(veronica.getRole()))

    winston.setWritePermissions(monitor.assignWritePermission(winston.getRole()))
    kelan.setWritePermissions(monitor.assignWritePermission(kelan.getRole()))

    nelson.setWritePermissions(monitor.assignWritePermission(nelson.getRole()))
    kelsie.setWritePermissions(monitor.assignWritePermission(kelsie.getRole()))

    howard.setWritePermissions(monitor.assignWritePermission(howard.getRole()))
    stefania.setWritePermissions(monitor.assignWritePermission(stefania.getRole()))

    willow.setWritePermissions(monitor.assignWritePermission(willow.getRole()))
    nala.setWritePermissions(monitor.assignWritePermission(nala.getRole()))

    stacy.setWritePermissions(monitor.assignWritePermission(stacy.getRole()))
    keikilana.setWritePermissions(monitor.assignWritePermission(keikilana.getRole()))

    kodi.setWritePermissions(monitor.assignWritePermission(kodi.getRole()))
    malikah.setWritePermissions(monitor.assignWritePermission(malikah.getRole()))

    caroline.setWritePermissions(monitor.assignWritePermission(caroline.getRole()))
    pawel.setWritePermissions(monitor.assignWritePermission(pawel.getRole()))

    for user in registeredUsers:
        if (loggedInUser == user.getUsername()):
            print("Username (ID): " + user.getUsername())
            print("Role: " + user.getRole())
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
main()