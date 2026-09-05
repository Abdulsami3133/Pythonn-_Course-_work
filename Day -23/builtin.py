'''
import sys

print(sys.argv)
print(sys.version)
print(sys.path)
print("start")
sys.exit()
print("end")


import platform

print(platform.system)
print(platform.release)
print(platform.processor)


import math

print(math.pi)
print(math.e)

print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))
print(math.factorial(5))
print(math.gcd(8,12))
print(math.sqrt(36))
print(math.pow(2,3))

import math

print(round(12.666666))
print(round(12.99999999999))

print(math.ceil(12.00000000000001))
print(math.ceil(12.3))
print(math.ceil(12.6666))
print(math.ceil(12.999999999))

print(math.floor(12.000000000001))
print(math.floor(12.3))
print(math.floor(12.666666))
print(math.floor(12.999999999))

import random

print(random.random())#float 0.0 to 1.0
print(random.randint(1,100))#int 1 to 100
print(random.uniform(1,6))#float 1 to 6

l = ['r','p','s']
print(random.choice(l))

ln = ['heads','tails']
print(random.choice(ln))

lang = ['python','java','css','javascript','flask']
print(random.choices(lang))#give random from the list

random.shuffle(lang)#shuffle the items in them
print(lang)

from collections import Counter

s = 'python programming'
res = Counter(s)
print(res)

from collections import Counter,defaultdict

products = ['sugar','salt','milk']
res = defaultdict(list)

for i in products:
    res[i].append(['des','rev','com'])
print(res)

from collections import Counter,defaultdict
s = 'python programming'
d = defaultdict(int)

from collections import Counter,defaultdict,deque

l  = deque([])

l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(60)
l.pop()
print(l)
'''
name = input("Enter the name: ")
dob = int(input("Enter the Date of Birth(DD-MM-YYYY): "))

year = dob.split("-")[-1]

pwd = name.capitalize()+"@"+year
print(pwd)