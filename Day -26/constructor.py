'''
class Instagram:
    def __init__(self, username, pwd):
        self.username = username
        self.pwd = pwd
        print(f"Welcome to Instagram, {self.username}")


sam = Instagram('Sami', '3133')
'''
class Instagram:

    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.post = []

    def getpassword(self):
        return self.__password

    def setpassword(self, newpassword):
        self.__password = newpassword

    @property
    def accesspost(self):
        return self.post

    @accesspost.setter
    def accesspost(self, newpost):
        self.post = newpost


sami = Instagram('sami', '3133')

# Username
print(sami.username)

# Password
print(sami.getpassword())

# Posts
print(sami.accesspost)

# Change username
sami.username = 'Sami_3133'
print(sami.username)

# Change password
sami.setpassword('sami@3133')
print(sami.getpassword())

# Add/change posts using property setter
sami.accesspost = ['Hello Instagram', 'My First Post']
print(sami.accesspost)