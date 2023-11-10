class User:
    def __init__(self, name, role) -> None:
        self.name = name
        self.role = role
        self.readPermissions = []
        self.writePermissions = []
    
    def __str__(self) -> str:
        return f"{self.name} ({self.role})\nRead Permissions: {self.readPermissions}\nWrite Permissions: {self.writePermissions}"
    
    def addReadPermissions(self, elem):
        self.readPermissions.append(elem)

    def addWritePermissions(self, elem):
        self.writePermissions.append(elem)