Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = input()
codegnan
a
'codegnan'
a  = input()
123
a
'123'
a = input()
a = input()
a = input("Enter the values:")
Enter the values:asdfaedfar14efasr324q234rasd
a
'asdfaedfar14efasr324q234rasd'
marks = input("Enter the marks:")
Enter the marks:99
marks
'99'
marks = int(input("Enter the marks:"))
Enter the marks:100
marks
100
price = float(input("Enter the Price:"))
Enter the Price:12
price
12.0
cgpa = float(input("Enter thr CGPA:"))
Enter thr CGPA:7.5
cgpa
7.5
names = input()
sam kim wax
names
'sam kim wax'
names = input().split()
sam waxz wad
names
['sam', 'waxz', 'wad']
names.split(',')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    names.split(',')
AttributeError: 'list' object has no attribute 'split'
names = input().split(',')
sam waxs wad
names
['sam waxs wad']
course = 'python-java-v'
course.split('-')
['python', 'java', 'v']
course
'python-java-v'
ss = 'communitcation quicklearner'
ss.split(',')
['communitcation quicklearner']
ss
'communitcation quicklearner'
names = input("Enter names:")
Enter names:sam wax zad
names
'sam wax zad'
names = input("Enter names:").split()
Enter names:sam wax zasd
names
['sam', 'wax', 'zasd']
names = tuple(input("Enter names:"))
Enter names:sam wax zasd
names
('s', 'a', 'm', ' ', 'w', 'a', 'x', ' ', 'z', 'a', 's', 'd')
names = tuple(input("Enter names:")).split()
Enter names:sam wax zasd
SyntaxError: multiple statements found while compiling a single statement
names = tuple(input("Enter names:")).split()
Enter names:sam wax zad
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    names = tuple(input("Enter names:")).split()
AttributeError: 'tuple' object has no attribute 'split'
names = tuple(input("Enter names:").split())
Enter names:sam wax
names
('sam', 'wax')
marks = input().split()
12 12 32 21
marks
['12', '12', '32', '21']
map(int,marks)
<map object at 0x0000015D2F3FF8C0>
list(map(int,marks))
[12, 12, 32, 21]
marks = list(map(int,input("Enter the marks:")))
Enter the marks:12 898 23 43 12 54 59 32
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    marks = list(map(int,input("Enter the marks:")))
ValueError: invalid literal for int() with base 10: ' '
marks = list(map(int,input("Enter the marks:").split()))
Enter the marks:12 33 22 55 22
marks
[12, 33, 22, 55, 22]
marks = tuple(map(int,input("Enter the marks:").split()))
Enter the marks:12 333 111 22 3212312\
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    marks = tuple(map(int,input("Enter the marks:").split()))
ValueError: invalid literal for int() with base 10: '3212312\\'
marks = tuple(map(int,input("Enter the marks:").split()))
Enter the marks:11 22 33 44 55
marks
(11, 22, 33, 44, 55)
marks = set(map(int,input("Enter the marks:").split()))
Enter the marks:123123 1233423
marks
{123123, 1233423}
a,b = [1,2]
a
1
b

b
2
a,b,c=[1,2,'str']
a
1
b
2
c
'str'
em,ps = input("Enter Em & pswd:").split()
Enter Em & pswd:sam@gmail.com 12
em
'sam@gmail.com'
ps
'12'
nm,mk = input("Enter NM & MK:").split()
Enter NM & MK:sam 99
nm
'sam'
mk
'99'
int(nm)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    int(nm)
ValueError: invalid literal for int() with base 10: 'sam'
>>> int(mk)
99
>>> a,b,c = list(map(int,input().split()))
12 123 1234
>>> a
12
>>> b
123
>>> c
1234
>>> status = eval(input())
True
>>> status
True
>>> type(status)
<class 'bool'>
>>> status = eval(input())
2+3j
>>> status
(2+3j)
>>> type(status)
<class 'complex'>
>>> status = eval(input())
[1,2,3,4]
>>> status
[1, 2, 3, 4]
>>> type(status)
<class 'list'>
>>> status = eval(input())
(1,2,3,4)
>>> status
(1, 2, 3, 4)
>>> type(status)
<class 'tuple'>
>>> status = eval(input())
{1:1,2:2,3:3,4:4}
>>> status
{1: 1, 2: 2, 3: 3, 4: 4}
>>> type(status)
<class 'dict'>
