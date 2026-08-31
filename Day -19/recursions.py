'''
def dis(n):
    while n<11:
        print(11-n)
        n+=1
dis(1)        

def dis(n):
    if n ==11:
        return
    dis(n+1)
    print(n)

dis(1)

def dis(s,ind):
    if ind ==len(s):
        return
    dis(s,ind+1)
    print(s[ind],end=" ")

dis("Codegnan",0)


def dis(s,ind,w):
    if len(s)-w+1==ind:
        return
    print(s[ind:ind+w])
    dis(s,ind+1,w)

s = input("Enter the string: ")
w = input("enter the width: ")
dis(s,0,w)    

def dis(l,ind):
    if ind == len(l):
        return 0
    return l[ind]+dis(l,ind+1)

l=[4,23,2,34,28,90]
print(dis(l,0))



def dis(l):
    if l==0:
        return 0
    return l%10 + dis(l//10)

l=43567
print(dis(l))

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))
print(fact(4))

a,b = 0,1
print(a,b)
for i in range(8):
    a,b=b,a+b
    print(b)

n = int(input("Enter the number: "))
if n==1:
    print(0)
elif n==2:
    print(0,1)
else:
    a,b=0,1
    print(a,b)
    for i in range(n-2):
        a,b=b,a+b
        print(b,end=' ') 
'''
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return fib(n-1)+fib(n-2)

for i in range(20):
    print(fib(i))         