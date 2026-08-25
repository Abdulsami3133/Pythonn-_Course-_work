'''
i =1
while i<=10:
    print(i)
    i+=1

i =10
while i>0:
    print(i)
    i-=1    
  

i = 10
while i<=100:
    print(i)
    i+=10

s = 'while loop'
i=0
while i>len(s)-1:
    print(s[i])
    i-=1


l = [5467,5678,6789,987]
i = 0
while i<len(l):
    print(l[i])
    i+=1    
    
n = 8765
while n>0:
    print(n%10)
    n//=10

n = 98765432456
a=0
while n>0:
    a+=n%10
    n//=10
    print(a)

n = 34567
a =1
while n >0:
    a*=n%10
    n//=10
print(a)    

n = 34567
res =0
while n >0:
    rem=n%10
    res =res*10+rem
    n//=10
print(res)    



n = int(input("Enter a number:"))
res =0
while n >0:
    rem=n%10
    if rem%2==0:
        res+=rem
    n//=10
print(res)    

l = [7,9,23,0,0,0,12,0,13,0,1,0,0,1,2,5,6,6,13,0]
while 0 in l:
    l.remove(0)
print(l)    

l = [2,3,6,76,12,4,1,5,61,4,5,2,23]
i=0
j=len(l)-1
while i<=j:
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j]) 
    i+=1
    j-=1       
'''
data = {
    'salt':50,
    'sugar':80,
    'Oil':150,
    'Chilli':100,
    'rice':1700,
    'butter':130,
    'bread':200,
    'wheatfloor':100
}
for i in data:
    print(i.ljust(20),data[i])
bill = 0
while True:
    prod = input("Enter the product name or [E]xit:")
    if prod == 'E' or prod == 'e':
        print("--------------------Bill---------------------------")
        print("Thanks for shopping")
        print("Total bill:",bill)
        break
    else:
        qnt = int (input("Enter the quantity: "))
        bill+=data[prod]*qnt  
