from user import User
from ldap import LDAP
import os
import time

class parser:

    filePath = None
    fileInput = None

    keys = None 

    userArray = []

    def __init__(self, fileIn, fileOut, maxAccounts):
        
        self.filePath = fileIn
        print(f"Reading file: {fileIn}\n")
        self.readFile()
        self.getKeys()
        self.parseUsers()
        if fileOut == "":
            fileOut = f"{os.getcwdb().decode()}/{str(time.time()).split('.')[0]}.ldf"
        if int(maxAccounts) > 100000:
            maxAccounts = 100000
        print(f"Writing file: {fileOut}")
        LDAP(self.keys, self.userArray, fileOut, int(maxAccounts))
        print(f"Finished ....")

    def readFile(self):
        file = open(self.filePath, "r")
        self.fileInput = file.readlines()
        file.close()

    def getKeys(self):
        self.keys = self.fileInput[0].strip("\n").split(",")

    def parseUsers(self):
        for i in range(1, len(self.fileInput)):
            self.userArray.insert((i-1), self.fileInput[i].strip("\n").split(","))


if __name__ == "__main__":
    fileOut = input("Outputfile: ")
    Accounts = input("How many Accounts (max 100000): ")

    parser(f"{os.getcwdb().decode()}/users_big.csv", fileOut, Accounts)