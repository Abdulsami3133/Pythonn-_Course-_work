'''
def dis(n):
    n+=10
    print("Inside:",n)

n=10
dis(n)
print("Outside:",n)

def dis(n):
    n+=10.3
    print("Inside:",n)

n=10.3
dis(n)
print("Outside:",n)

def dis(n):
    n+='Lang'
    print("Inside:",n)

n='Python '
dis(n)
print("Outside:",n)

def dis(n):
    n=[1,2,3,4]
    n.append(5)
    print("Inside:",n)

n=[1,2,3,4,5]
dis(n)
print("Outside:",n)

def dis(n):
    n={1,2,3,4}
    n.add(5)
    print("Inside:",n)

n={1,2,3,4,5}
dis(n)
print("Outside:",n)
'''
def dis(n):
    n[5]=6
    print("Inside the function:",n)

n = {1:2,3:4}
dis(n)
print("Outside the function:",n)
    