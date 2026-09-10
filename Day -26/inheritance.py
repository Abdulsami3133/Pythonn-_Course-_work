class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload the status for 24hr")

class whatsappv3(whatsappv1):
    def groups(self):
        print("You can create  group and talk to multiple people")  

class whatsappv4(whatsappv1):
    def community(self):
        print("You can multiple groups")

class whatsappv5(whatsappv3,whatsappv4,whatsappv1,whatsappv2):
    def channels(self):
        print("ypu can post regularly and news")        



sam = whatsappv5()
sam.message()
sam.status()
sam.groups()
sam.community()
sam.channels()