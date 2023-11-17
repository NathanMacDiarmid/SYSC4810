import csv

class ReferenceMonitor:
    def __init__(self) -> None:
        with open("\Documents\School\SYSC4810\AccessControlMatrix.csv", "r") as CSVFile:
            CSVReader = csv.DictReader(CSVFile)
            dataDict = [row for row in CSVReader]
            newDict = {}
            for item in dataDict:
                role = item.pop("Role")
                newDict[role] = item
        self._permissions = newDict
    
    def assignReadPermission(self, userRole) -> list:
        if (userRole in self._permissions):
            lst = []
            for i in self._permissions.get(userRole):
                if (self._permissions.get(userRole)[i] == "R"):
                    lst.append(i)
                elif (self._permissions.get(userRole)[i] == "RW"):
                    lst.append(i)
            return lst
        else:
            return []
    
    def assignWritePermission(self, userRole) -> list:
        if (userRole in self._permissions):
            lst = []
            for i in self._permissions.get(userRole):
                if (self._permissions.get(userRole)[i] == "W"):
                    lst.append(i)
                elif (self._permissions.get(userRole)[i] == "RW"):
                    lst.append(i)
            return lst
        else:
            return []