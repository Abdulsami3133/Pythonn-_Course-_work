'''

  0 1 2 3 4
0 * * * * *
1 *       *
2 *       *
3 *       *
4 * * * * *


n = int(input("Enter the size: "))#D
if n >2:
    for i in range(n):
        for j in range(n):
            if i==0 or j==0 or i==n-1 or j==n-1:
                print("*",end=' ')
            else:
                print(" ",end=" ")

        print()            
else:
    print("Enter number greater than {n}",n)   
         
n = int(input("Enter the size: "))
m = n//2
if n>2:
    for i in range(n):
        for j in range(n):
            if i==0 or j==0  or i ==n-1 or i==n:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()            

n = int(input("Enter the size: ")) #F
m = n//2
if n>2:
    for i in range(n):
        for j in range(n):
            if i==0 or j==0  or i==m:
                print("*",end=" ")
            else:
                print(" ",end=" ")
                
        print()
else:
    print("Enter a lager number than ",n)

n = int(input("Enter the size: ")) #C
m = n//2
if n>2:
    for i in range(n):
        for j in range(n):
            if i==0 or j==0  or i ==n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
else:
    print("Enter a number larger than  ",n) 

n = int(input("Enter the size: ")) #G
m = n//2
if n>2:
    for i in range(n):
        for j in range(n):
            if i==0 or j==0  or i ==n-1 or (j==n-1 and i>=m) or (i==m and j>=m):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
else:
    print("Enter a number larger than  ",n)            

n = int(input("Enter the size: "))#H
m = n//2
if n>2:
    for i in range(n):
        for j in range(n):
            if j==0 or j==n-1 or i == n//2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
else:
    print("Enter a number larger than  ",n)

n = int(input("Enter the size: ")) #I

if n > 2:
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == n // 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
else:
    print("Enter a number larger than", n) 


n = int(input("Enter the size: ")) #J

if n > 2:
    for i in range(n):
        for j in range(n):
            if i == 0 or j == n // 2 or (i == n - 1 and j < n // 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
else:
    print("Enter a number larger than", n)

n = int(input("Enter the size: ")) #Z
m = n//2
if n>2:
    for i in range(n):
        for j in range(n):
            if i==0  or i ==n-1 or i+j == n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
else:
    print("Enter a number larger than  ",n)

n = int(input("Enter the size: "))#X

if n > 2:
    for i in range(n):
        for j in range(n):
            if j == i or j == n - i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
else:
    print("Enter a number larger than", n)  

n = int(input("Enter the size: "))#Y

if n > 2 and n%2!=0:
    for i in range(n):
        for j in range(n):
            if (j == i and i <= n // 2) or (j == n - i - 1 and i <= n // 2) or (j == n // 2 and i > n // 2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
else:
    print("Enter must be odd and a number larger than", n)

n = int(input("Enter the size: "))#K

if n > 2:
    for i in range(n):
        for j in range(n):
            if j==0 or (i==n//2 and j<=n//2) or (i==j and i>=n//2) or (i+j==n-1 and i<=n//2):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
else:
    print("Enter a number larger than", n) 

n = int(input("Enter the size: "))#S

if n > 2:
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n // 2 or i == n - 1:
                print("*", end=" ")
            elif i < n // 2 and j == 0:
                print("*", end=" ")
            elif i > n // 2 and j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
else:
    print("Enter a number larger than", n)         

n = int(input("Enter the size: "))#M

if n > 2:
    for i in range(n):
        for j in range(n):
            if j==0 or  j==n-1 or (i==j and i<=n//2) or i+j==n-1 and i<=n//2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
else:
    print("Enter a number larger than", n)


n = int(input("Enter the size: "))  # N

if n > 2:

    for i in range(n):

        for j in range(n):

            if j == 0 or j == n - 1 or i == j:
                print("*", end=" ")

            else:
                print(" ", end=" ")

        print()

else:
    print("Enter a number larger than", n)

n = int(input("Enter the size: "))  # A

if n > 2:

    for i in range(n):

        for j in range(n):

            if i == 0 and j == n // 2:
                print("*", end=" ")

            elif i > 0 and i < n // 2 and (j == n // 2 - i or j == n // 2 + i):
                print("*", end=" ")

            elif i == n // 2:
                print("*", end=" ")

            elif i > n // 2 and (j == 0 or j == n - 1):
                print("*", end=" ")

            else:
                print(" ", end=" ")

        print()

else:
    print("Enter a number larger than", n)

n = int(input("Enter the size: "))  # V

if n > 2:

    for i in range(n):

        for j in range(n):

            if (j == i and i <= n // 2) or (j == n - i - 1 and i <= n // 2):
                print("*", end=" ")

            else:
                print(" ", end=" ")

        print()

else:

    print("Enter a number larger than", n)
'''
n = int(input("Enter the size: "))  # B

if n > 2:

    for i in range(n):

        for j in range(n):

            if (j == 0 or
                (i == 0 and j < n - 1) or
                (i == n // 2 and j < n - 1) or
                (i == n - 1 and j < n - 1) or
                (j == n - 1 and i > 0 and i < n - 1 and i != n // 2)):

                print("*", end=" ")

            else:

                print(" ", end=" ")

        print()

else:

    print("Enter a number larger than", n)    