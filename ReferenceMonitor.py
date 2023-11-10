import csv
import User

with open("\Documents\School\SYSC4810\AccessControlMatrix.csv", "r") as CSVFile:
    CSVReader = csv.DictReader(CSVFile)
    dataDict = [row for row in CSVReader]

print(dataDict[1]["Role"])