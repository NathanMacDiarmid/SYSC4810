import csv

class ReferenceMonitor:
    def __init__(self) -> None:
        with open("AccessControlMatrix.csv", "r") as CSVFile:
            CSVReader = csv.DictReader(CSVFile)
            dataDict = [row for row in CSVReader]
            newDict = {}
            for item in dataDict:
                role = item.pop("Role")
                newDict[role] = item
        self.permissions = newDict
    
    def assignReadPermission(self, userRole) -> list:
        if (userRole in self.permissions):
            lst = []
            for i in self.permissions.get(userRole):
                if (self.permissions.get(userRole)[i] == "R"):
                    lst.append(i)
                elif (self.permissions.get(userRole)[i] == "RW"):
                    lst.append(i)
            return lst
        else:
            print("Not a valid role")
            return []
    
    def assignWritePermission(self, userRole) -> list:
        if (userRole in self.permissions):
            lst = []
            for i in self.permissions.get(userRole):
                if (self.permissions.get(userRole)[i] == "W"):
                    lst.append(i)
                elif (self.permissions.get(userRole)[i] == "RW"):
                    lst.append(i)
            return lst
        else:
            print("Not a valid role")
            return []