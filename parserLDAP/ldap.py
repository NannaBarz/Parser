from user import User

class LDAP:

    keys = None
    userdata = None
    outputfile = None
    maxUsers = None
    ladpUsersUnfiltered = []
    ladpUsersFiltered = []

    def __init__(self, keys, userdata, output, maxUsers):
        self.keys = keys
        self.userdata = userdata
        self.outputfile = output
        self.maxUsers = maxUsers
        self.run()

    def run(self):
        if self.maxUsers > len(self.userdata):
            self.maxUsers = len(self.userdata)
        fileOut = open(self.outputfile, "w")
        for i in range(0, len(self.userdata)):
            self.genLdfAnja(User(self.keys, self.userdata[i]))
        self.filter()
        self.writeFile(fileOut, self.maxUsers)
        fileOut.close()    

    def genLdfAnja(self, userObject):
        ldapObject = []
        ldapObject.append(f"dn: CN={userObject.getValue('GivenName')} {userObject.getValue('Surname')},OU=person,DC=octest,DC=local\n")
        ldapObject.append(f"changetype: add\n")
        ldapObject.append(f"objectClass: top\n")
        ldapObject.append(f"objectClass: person\n")
        ldapObject.append(f"objectClass: organizationalPerson\n")
        ldapObject.append(f"objectClass: user\n")
        ldapObject.append(f"cn: {userObject.getValue('GivenName')} {userObject.getValue('Surname')}\n")
        ldapObject.append(f"sn: {userObject.getValue('Surname')}\n")
        ldapObject.append(f"givenName: {userObject.getValue('GivenName')}\n")
        ldapObject.append(f"distinguishedName: CN={userObject.getValue('GivenName')} {userObject.getValue('Surname')},OU=person,DC=octest,DC=local\n")
        ldapObject.append(f"displayName: {userObject.getValue('GivenName')} {userObject.getValue('Surname')}\n")
        ldapObject.append(f"name: {userObject.getValue('GivenName')} {userObject.getValue('Surname')}\n")
        ldapObject.append(f"sAMAccountName: {userObject.getValue('GivenName')}.{userObject.getValue('Surname')}\n")
        ldapObject.append(f"userPrincipalName: {userObject.getValue('GivenName')}.{userObject.getValue('Surname')}@octest.local\n")
        ldapObject.append(f"objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=octest,DC=local\n")
        ldapObject.append(f"\n\n")
        self.ladpUsersUnfiltered.append(ldapObject)

    def filter(self):
        counter = 0
        tempArray = []
        for i in range(0, len(self.ladpUsersUnfiltered)):
            found = False
            for c in range(0, len(tempArray)):
                try:
                    a = tempArray[c][12]
                    b = self.ladpUsersUnfiltered[i][12]
                    if a == b:
                        found = True
                        break
                except:
                    pass
            if found == False:
                counter += 1    
                tempArray.append(self.ladpUsersUnfiltered[i])
                if counter == self.maxUsers:
                    break
        self.ladpUsersFiltered = tempArray        
                
    def writeFile(self, fileObject, maxAccounts):
        for i in range(0, len(self.ladpUsersFiltered)):
            for c in range(0, len(self.ladpUsersFiltered[i])):
                fileObject.write(self.ladpUsersFiltered[i][c])
            fileObject.write("\n")
    