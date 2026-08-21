#str list tuple set dict range
'''
for var in seq:
   #stmts

----------------------------------------------
   
s = 'python programming'
for i in s:                #for str
    print(i)


l = [1,2,3,4,5]
for num in l:                #for list
    print(num)



pr = (9876,4567,567,321)     #for tuple
for pre in pr:
    print(pre)


names = {'mounasri','usharani','lohitha'}
for name in names:                          #for set
    print(name)


d = {1:2,2:4,3:6,4:8,5:10}
for i in d:                 #for Dict
    print(i,d[i])
-------------------------------------
range(start,end+1,step):(0,,1)

                          
for i in range(1,11):               #for range
    print(i)

for i in range(2,21,2):
    print(i)

for i in range(5,101,5):
    print(i)

for i in range(5,0,-1):
    print(i)

for i in range(19,0,-2):
    print(i)

printing Index

s = 'python programming language'
for i in range(len(s)):                
    print(i,s[i])

s = (456,4567,4567,543,3456)
for i in range(len(s)):
    print(i,s[i])
    
s = 'python programming'
for i in enumerate(s):                
    print(i)
    

s = [6789,4567,6798,7689]
for i in enumerate(s):
    print(i[0],i[1])



d = {1:2,2:4,3:6,4:8,5:10}
for i in enumerate(d):
    print(i[0],i[1],d[i[1]])
 
for i in range(1,11):
    if i == 5:
        break
    print(i)11

for i in range(1,11):
    if i ==5:
        continue
    print(i)

for i in range(1,11):
    if i == 52:
        break
    print(i)
else:
    print("End of the loop")

l = [12,23,12,23,16,43,54]
n = 16
for i in l:
    if i == n:
        print(n,"found at index")
        break
else:
        print(n,"not found")
        

pin = 3121
for i in range(5):
    epin = int(input("Enter the pin:"))
    if epin == pin:
        print("Unlock phone")
    else:
         print("Invalid pin")
else:
    print("Try after 30 seconds")
'''
n = int(input("Enter a number:"))
for i in range(2,n//2+1):
    if n%i==0:
        print("Not  Prime Number")
        break
else:
    print("Prime Number")
    
