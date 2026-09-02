'''
Generators are the way to create"generative" code -they generate values one by one instead of creating everything at once

def reels():
    data = ['1..100','101..200','201..300','301..400','401..500']
    for i in data:
        yield i

res = reels()

print(next(res))
print(next(res))
print(next(res))


def cd():
    yield 5
    yield 4
    yield 3
    yield 2
    yield 1

res = cd()
for i in res:
    print(i)

def fact(n):
    for i in range(1,n+1):
        if n%2==0:
            yield i
res  = fact(16)
for i in res:
    print(i)                

def prime(n):
    for i in range(2,n+1):
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            yield i

res = prime(100)
for i in res:
    print(i,end=' ')

l = [i for i in range(1,11)]
print(l)

m = [i for i in range(2,11,2)]
print(m)

n=16
f = [i for i in range(1,n+1) if n%i==0]
print(f)

x = [1,2,3,4,5,6,7,8,9,10]
y = [i if i%2==0 else 0 for i in x]
print(y)

l = [[j for j in range(1,4)] for i in range(3)]
print(l)
'''
s = {i:i*i for i in range(1,11)}
print(s)