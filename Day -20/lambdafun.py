'''
wish = lambda name:f'welcome to the course {name}'
print(wish("Abdul"))
print(wish("Sami"))

gst = lambda price:price+price*0.18
print(gst(1000))
print(gst(2000))

avg = lambda a,b,c:(a+b+c)/3
print(avg(3,4,5))
print(avg(20,70,60))

iseven = lambda a: "Even" if a%2==0 else "Odd"
print(iseven(789))
print(iseven(22))

lrg = lambda a,b,c: a if a>b and a>c else(b if b>c else c)
print(lrg(23,54,34))
print(lrg(7,5,3))

isvowel  = lambda a: "Vowel" if a in "aeiouAEIOU" else "Cons"
print(isvowel('a'))
print(isvowel('v'))

l=[1,2,3,4,5,6,7]
print(l)
up = list(map(lambda i:i+10,l))
print(up)

t=(234,567,432,756,789)
print(t)
dis = list(map(lambda i:i-i*0.3,t))
print(dis)


l=[1,2,3,4,5,6,7]
print(l)
up = list(filter(lambda i:i%2!=0,l))
print(up)

t=(234,5671,432,7566,789)
print(t)
dis = list(filter(lambda i:i>1000,t))
print(dis)


l = ['sami@codegnan.com','sami@yahoo.com','sami@gmail.com','sami@outlook.com']
res  = list(map(lambda i:i.split('@')[-1],l))
print(res)


from functools import reduce

l = [4,2,4,64,75,2,4645,8]

res = reduce(lambda sum,i:sum+i,l)
print(res)

res1 = reduce(lambda pro,i:pro*i,l)
print(res1)

seats = {'s1':True,
         's2':False,
         's3':False,
         's4':False,
         's5':True,
         's6':True}
ava = list(filter(lambda i:seats[i]!=True,seats))
print(ava)

pro ={
    'eggs':80,
    'sugar':60,
    'salt':20,
    'butter':40,
    'milk':30
}
res = list(filter(lambda i:pro[i]>50,pro))
print(res)
'''
pro ={
    'eggs':80,
    'sugar':60,
    'salt':20,
    'butter':40,
    'milk':30
}
print(dict(sorted(pro.items(),key = lambda i:i[1])))
print(dict(sorted(pro.items(),key = lambda i:i[1],reverse=True)))