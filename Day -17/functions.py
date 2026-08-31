'''
def function_name(arg):
  #stsmt
  return(opt)
function_name(para)


def gst(price):
    print("Original Price:",price)
    print("Final Price:",price+price*0.18)
gst(1700)
gst(100) 
gst(1000)
gst(5000)
gst(2500)  

def table(n):
    print()
    print(f'{n}-Table')
    print("----------------------")
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')
        

for i in range(1,21):
    table(i)   

def isleap(year):
    if year%400==0 or(year%4==0 and year%100!=0):
        return " Leap Year"
    else:
        return "Not a Leap Year"

print(isleap(2012))
print(isleap(2020))
print(isleap(2024))
print(isleap(2026))              

def isprime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return"Not a Prime Number"

        return"Prime Number"
print(isprime(1))
print(isprime(12))
print(isprime(32))
print(isprime(23))

def dis(name,email,pwd): # Positional
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)
dis('sam','sam@123.com','sam@1234')
dis('sam@123.com','sam','sam@1234')
dis('sam@1234','sam','sam@123.com')

def dis(name,email,pwd): # Keyword
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)
dis(name='sam',email='sam@123.com',pwd='sam@1234')
dis(email='sam@123.com',name='sam',pwd='sam@1234')
dis(pwd='sam@1234',name='sam',email='sam@123.com')


def dis(name,email,pwd=None): # None
    print("name:",name)
    print("email:",email)
    print("pwd:",pwd)
dis('sam','sam@123.com',)
dis('sam','sam@123.com','sam@1234')

def display(*names):
    print(names)

display("sam")
display("sam","zaib")
display("sami","zaib","ayub")
display("sami","zaib","ayub","vali")    
'''
def display(**names): # output as Dict
    print(names)

display(n1="sam")
display(n1="sam",n2="zaib")
display(n1="sami",n2="zaib",n3="ayub")
display(n1="sami",n2="zaib",n3="ayub",n4="vali")        