from user import User

class LDAP:

    keys = None
    userdata = None
    outputfile = None
    maxUsers = None

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
        for i in range(0, self.maxUsers):
            self.genLdfAnja(fileOut, User(self.keys, self.userdata[i]))
        fileOut.close()    

    def genLdfAnja(self, fileObject, userObject):
        fileObject.write(f"dn: CN={userObject.getValue('GivenName')} {userObject.getValue('Surname')},OU=person,DC=octest,DC=local\n")
        fileObject.write(f"changetype: add\n")
        fileObject.write(f"objectClass: top\n")
        fileObject.write(f"objectClass: person\n")
        fileObject.write(f"objectClass: organizationalPerson\n")
        fileObject.write(f"objectClass: user\n")
        fileObject.write(f"cn: {userObject.getValue('GivenName')} {userObject.getValue('Surname')}\n")
        fileObject.write(f"sn: {userObject.getValue('Surname')}\n")
        fileObject.write(f"givenName: {userObject.getValue('GivenName')}\n")
        fileObject.write(f"distinguishedName: CN={userObject.getValue('GivenName')} {userObject.getValue('Surname')},OU=person,DC=octest,DC=local\n")
        fileObject.write(f"displayName: {userObject.getValue('GivenName')} {userObject.getValue('Surname')}\n")
        fileObject.write(f"name: {userObject.getValue('GivenName')} {userObject.getValue('Surname')}\n")
        fileObject.write(f"sAMAcountName: {userObject.getValue('GivenName')}.{userObject.getValue('Surname')}\n")
        fileObject.write(f"userPrincipalName: {userObject.getValue('GivenName')}.{userObject.getValue('Surname')}@octest.local\n")
        fileObject.write(f"objectCategory: CN=Person,CN=Schema,CN=Configuration,DC=octest,DC=local\n")
        fileObject.write(f"\n")



    