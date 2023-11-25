class User:
    def __init__(self, username, name, role) -> None:
        self.__username = username
        self.__name = name
        self.__role = role
        self.__readPermissions = []
        self.__writePermissions = []
    
    def getUsername(self) -> str:
        return self.__username
    
    def getName(self) -> str:
        return self.__name
    
    def getRole(self) -> str:
        return self.__role
    
    def setReadPermissions(self, permissions) -> None:
        self.__readPermissions = permissions

    def setWritePermissions(self, permissions) -> None:
        self.__writePermissions = permissions

    def getReadPermissions(self) -> list:
        return self.__readPermissions
    
    def getWritePermissions(self) -> list:
        return self.__writePermissions