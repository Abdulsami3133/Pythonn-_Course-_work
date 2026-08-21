'''
s = 'python programming'
d = {}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)        
-----------------------------------------------------
s = 'aaaaaaasssssssdddddbbcccctt'
c=1
res = ''
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c+=1
    else:
        res+=s[i]+str(c)
        c=1
print(res+s[i]+str(c))        
-----------------------------------
if 10==10:
    pass

for i in range(1,20):
    pass

def verify():
    pass

class verify:
    pass
------------------------------------------------------------
'''
email = 'aasdasd'
password = '12312'
amount = 20000
assert amount>0,"Amount needs to be +ve"
assert email!='' and password!='','userneeds to give email and pwd'
