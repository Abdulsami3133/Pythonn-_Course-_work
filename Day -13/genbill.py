data = {
    'salt':50,
    'sugar':80,
    'Oil':150,
    'Chilli':100,
    'rice(25kg)':1700,
    'butter':130,
    'bread':200,
    'wheatfloor':100
}
for i in data:
    print(i.ljust(20),data[i])

prods = input("Enter the product: ").split()
print("--------------------Bill---------------------------")
bill = 0
for i in prods:
    print(i.ljust(20),data[i])
    bill+=data[i]
print("Total bill".ljust(20),bill)    
