class User:

    keys = None
    values = None
    userDict = {}

    def __init__(self, keyarray, valuearray):
        self.keys = keyarray
        self.values = valuearray
        self.parse()

    def parse(self):
        for i in range(0, len(self.keys)):
            self.userDict.update({self.keys[i] : self.values[i]})

    def printUser(self):
        print(self.userDict)        

    def getValue(self, key):
        if key in self.userDict:
            return str(self.userDict[key])
        else:
            return "0"