import UI as ui
import User
import ReferenceMonitor
def main():
    monitor = ReferenceMonitor.ReferenceMonitor()

    testUser = User.User("Name Here", "Happy")
    #ui.renderUI()
    mischa = User.User("Mischa Lowery", "Client")
    veronica = User.User("Veronica Perez", "Client")

    winston = User.User("Winston Callahan", "Teller")
    kelan = User.User("Kelan Gough", "Teller")

    nelson = User.User("Nelson Wilkins", "Financial Advisor")
    kelsie = User.User("Kelsie Chang", "Financial Advisor")

    howard = User.User("Howard Linkler", "Compliance Officer")
    stefania = User.User("Stefania Smart", "Compliance Officer")

    willow = User.User("Willow Garza", "Premium Client")
    nala = User.User("Nala Preston", "Premium Client")

    stacy = User.User("Stacy Kent", "Investment Analyst")
    keikilana = User.User("Keikilana Kapahu", "Investment Analyst")

    kodi = User.User("Kodi Matthews", "Financial Planner")
    malikah = User.User("Malikah Wu", "Financial Planner")

    caroline = User.User("Caroline Lopez", "Technical Support")
    pawel = User.User("Pawel Barclay", "Technical Support")

    # Assign Read Permission

    testUser.readPermissions = monitor.assignReadPermission(testUser.role)

    mischa.readPermissions = monitor.assignReadPermission(mischa.role)
    veronica.readPermissions = monitor.assignReadPermission(veronica.role)

    winston.readPermissions = monitor.assignReadPermission(winston.role)
    kelan.readPermissions = monitor.assignReadPermission(kelan.role)

    nelson.readPermissions = monitor.assignReadPermission(nelson.role)
    kelsie.readPermissions = monitor.assignReadPermission(kelsie.role)

    howard.readPermissions = monitor.assignReadPermission(howard.role)
    stefania.readPermissions = monitor.assignReadPermission(stefania.role)

    willow.readPermissions = monitor.assignReadPermission(willow.role)
    nala.readPermissions = monitor.assignReadPermission(nala.role)

    stacy.readPermissions = monitor.assignReadPermission(stacy.role)
    keikilana.readPermissions = monitor.assignReadPermission(keikilana.role)

    kodi.readPermissions = monitor.assignReadPermission(kodi.role)
    malikah.readPermissions = monitor.assignReadPermission(malikah.role)

    caroline.readPermissions = monitor.assignReadPermission(caroline.role)
    pawel.readPermissions = monitor.assignReadPermission(pawel.role)

    # Assign Write Permission

    testUser.writePermissions = monitor.assignWritePermission(testUser.role)

    mischa.writePermissions = monitor.assignWritePermission(mischa.role)
    veronica.writePermissions = monitor.assignWritePermission(veronica.role)

    winston.writePermissions = monitor.assignWritePermission(winston.role)
    kelan.writePermissions = monitor.assignWritePermission(kelan.role)

    nelson.writePermissions = monitor.assignWritePermission(nelson.role)
    kelsie.writePermissions = monitor.assignWritePermission(kelsie.role)

    howard.writePermissions = monitor.assignWritePermission(howard.role)
    stefania.writePermissions = monitor.assignWritePermission(stefania.role)

    willow.writePermissions = monitor.assignWritePermission(willow.role)
    nala.writePermissions = monitor.assignWritePermission(nala.role)

    stacy.writePermissions = monitor.assignWritePermission(stacy.role)
    keikilana.writePermissions = monitor.assignWritePermission(keikilana.role)

    kodi.writePermissions = monitor.assignWritePermission(kodi.role)
    malikah.writePermissions = monitor.assignWritePermission(malikah.role)

    caroline.writePermissions = monitor.assignWritePermission(caroline.role)
    pawel.writePermissions = monitor.assignWritePermission(pawel.role)

    print(mischa)
    print(veronica)

    print(winston)
    print(kelan)

    print(nelson)
    print(kelsie)

    print(howard)
    print(stefania)

    print(willow)
    print(nala)

    print(stacy)
    print(keikilana)

    print(kodi)
    print(malikah)

    print(caroline)
    print(pawel)

    print(testUser)

main()