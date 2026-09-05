import random
name = input("Enter the name: ").title()
dob = input("Enter the Date of Birth(DD-MM-YYYY): ")
spc = ['@','!','#','$','%','&','*']
pwd = name+random.choice(spc)+dob[-4:]

print("Generated password: ",pwd)