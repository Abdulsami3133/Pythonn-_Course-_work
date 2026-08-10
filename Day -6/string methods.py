Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s = "Codegnan"
s
'Codegnan'
type(s)
<class 'str'>
s = ''
s
''
a = 'python'
b = 'programming'
a+b
'pythonprogramming'
b=' programming'
a+b
'python programming'
fname='abdul'
name=' sami'
fname+name
'abdul sami'
a
'python'
a*10
'pythonpythonpythonpythonpythonpythonpythonpythonpythonpython'
'*'20
SyntaxError: invalid syntax
'*'*20
'********************'
'-codegnan- '*4
'-codegnan- -codegnan- -codegnan- -codegnan- '

s = 'codenan'
s[3]
'e'
s[-2]
'a'
s[2]
'd'
s[-5]
'd'
names = 'kalyani vishupriya lakshmi mounasri lohitha usharani'
name
' sami'
names
'kalyani vishupriya lakshmi mounasri lohitha usharani'
names[]
SyntaxError: invalid syntax
SyntaxError: invalid syntax
SyntaxError: invalid syntax
name[:7]
' sami'
names[:7]
'kalyani'
names[8:19]
'vishupriya '
names[19:26]
'lakshmi'
names[27:35]
'mounasri'
names[36:43]
'lohitha'
names[44:len(names)]
'usharani'
names[-8:]
'usharani'
names[-16:-8]
'lohitha '
'kalyani' in names
True
'a' lohitha in names
SyntaxError: invalid syntax
"lohitha" in names
True
'a' in names
True
'z' in names
False
len(names)
52
ord('a')
97
ord('AZ')
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    ord('AZ')
TypeError: ord() expected a character, but string of length 2 found
chr(40)
'('
chr(1)
'\x01'
chr(2000)
'ߐ'

chr(414)
'ƞ'
sorted(names)
[' ', ' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'h', 'h', 'h', 'h', 'h', 'i', 'i', 'i', 'i', 'i', 'i', 'i', 'k', 'k', 'l', 'l', 'l', 'm', 'm', 'n', 'n', 'n', 'o', 'o', 'p', 'r', 'r', 'r', 's', 's', 's', 's', 't', 'u', 'u', 'u', 'v', 'y', 'y']
max(names)
'y'
min(names)
' '
a = 'sami'
upper(a)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    upper(a)
NameError: name 'upper' is not defined. Did you mean: 'super'?
a.upper()
'SAMI'
a = 'SAmi'
a.lower()
'sami'
a.swapcase()
'saMI'
a.capitalize()
'Sami'
a = ' i love python'
a.title()
' I Love Python'
a
' i love python'
a = 'I love python'
a
'I love python'
a.center(50,'-')
'------------------I love python-------------------'
s.ljust(40.'*')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
s.ljust(40,'*')
'codenan*********************************'
s.rjust(40,'*')
'*********************************codenan'
s= 65
s
65
s.zfill()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    s.zfill()
AttributeError: 'int' object has no attribute 'zfill'
s.zfill(2)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    s.zfill(2)
AttributeError: 'int' object has no attribute 'zfill'
'12'.zfill(5)
'00012'
s  = 'python programming language'
s
'python programming language'
s.find('python')
0
s.fing("g")
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    s.fing("g")
AttributeError: 'str' object has no attribute 'fing'. Did you mean: 'find'?
s.find('g')
10
s.find('p')
0
s.rfind('g')
25
>>> s.rfind("p")
7
>>> s.fing('a')
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    s.fing('a')
AttributeError: 'str' object has no attribute 'fing'. Did you mean: 'find'?
>>> s.find('f')
-1
>>> s.index('a')
12
>>> s.index('p')
0
>>> s.index('z')
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    s.index('z')
ValueError: substring not found
>>> s.count('a')
3
>>> s.count('p')
2
>>> s.rindex('g')
25
>>> s
'python programming language'
>>> s.replace('o','1')
'pyth1n pr1gramming language'
>>> s.replace('a','2')
'python progr2mming l2ngu2ge'
>>> s.replace('python','java')
'java programming language'
>>> s.maketrans('aeiou','#@$&*')
{97: 35, 101: 64, 105: 36, 111: 38, 117: 42}
>>> s.translate(s.maketrans('aeiou','#@$&*'))
'pyth&n pr&gr#mm$ng l#ng*#g@'
>>> b'Hello \xf0\x9f\x99\x82'.decode()
'Hello 🙂'
>>> txt = "Hello 🙂"
>>> txt.encode()
b'Hello \xf0\x9f\x99\x82'
