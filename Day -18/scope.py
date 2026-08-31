'''
def dis():
    n=10
    print("Inside function: ",n)

dis()
print("Outside function: ",n)    

def dis():
    cur = "PFS"
    def update():
        nonlocal cur
        cur = "JFS"
        print("Inner function:",cur)
    update()
    print("Outer function:",cur)
dis()        

l = [1,2,3,4,5]
print(max(l))

max =20
print(max)
'''
