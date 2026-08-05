Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> a
10
>>> b=10
>>> 
>>> b
10
>>> a,b,c=10,20,30
>>> a b c
SyntaxError: invalid syntax
>>> a
10
>>> b
20
>>> c
30
>>> a,b=b,a
>>> a
20
>>> a=10
>>> b=20
>>> a=b
>>> b
20
>>> a
20
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a=100
>>> b=200
