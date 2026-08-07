Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#python operatoers
a=10
b=5
a+b
15
a-b
5
a*b
50
a/2
5.0
9/2
4.5
9//2
4
2**2
4
2***2
SyntaxError: invalid syntax
a
10
a**b
100000
10.2//2
5.0
12.3/2
6.15
a**3
1000
2**3
8
16**2
256
a>b
True
a<b
False
a == b
False
a>=b
True
a<=b
False
a!=b
True
a!=a
False
a = 20
a+=10
a
30
a-=15
a
15
a*=a
a*=10
a=15
a
15
a*=10
a*=10







a=10
a
10
a *= 10
a
100
a  //=2
a
50
a **=2
a
2500
a/=2
a
1250.0

email =True
passw=False
email and passw
False
emain or pass
SyntaxError: invalid syntax
email or passw
True
login =True
login=False
display=Truw
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    display=Truw
NameError: name 'Truw' is not defined. Did you mean: 'True'?

display = True
login or display
True
's' in 'aeiou'
False
not 's' in 'aeiou'
True
7%2==0 and 3%2==0
False
6%2==0 and 3%2==0
False
6%2==0 or 3%2==0
True
3%2==1.5
False
3%2
1
1
1

# str list set dict
s = 'python programmin'
'python' in s
True
'java' in s
False
'z' in s
False
'a' in s
True
'c++' not in s
True
l=[1,2,3,4,5]
3 in l
True
9 not in l
True
1 not i l
SyntaxError: invalid syntax
1 not in l
False
t = (20,30,40,50)
50 in t
True
30 not in t
False
s = {'pen','paper','book'}
book in s
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    book in s
NameError: name 'book' is not defined. Did you mean: 'bool'?
'book' in s
True
'book' not in s
False
'pen' in s
True
data = {'name':'sam','batch':65,'course':'pfs'}
'sam' in data
False
'name' in data
True
65 in dat
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    65 in dat
NameError: name 'dat' is not defined. Did you mean: 'data'?
65 in data
False
l = [1,2,3,4]
m = [1,2,3,4]
id(l)
1775388159040
id(m)
1775388123712
 l == m
 
SyntaxError: unexpected indent
l == m
True
>>>  l is m
...  
SyntaxError: unexpected indent
>>> l is m
False
>>> n = m
>>> n
[1, 2, 3, 4]
>>> id(n)
1775388123712
>>> m is n
True
>>> m == n
True
>>> 
>>> 
>>> 11&12
8
>>> 11 | 15
15
>>> 11 ^ 12
7
>>> 2<<2
8
>>> 2<<3
16
>>> 2<<4
32
>>> 2<<4
32
>>> 16>>2
4
>>> 
>>> ~14
-15
>>> ~14
-15
>>> ~33
-34
>>> ~32
-33
