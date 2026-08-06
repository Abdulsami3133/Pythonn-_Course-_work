Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s={1,2,3,1,2,3,4}
s
{1, 2, 3, 4}
type(s)
<class 'set'>
l=[1,2,3]
l
[1, 2, 3]
type(l)
<class 'list'>
l.append(12)
l
[1, 2, 3, 12]
id(l)
2769213333632
l.append("END")
l
[1, 2, 3, 12, 'END']
t=(1,2,4,3,2,1,"saasd")
t
(1, 2, 4, 3, 2, 1, 'saasd')
type(t)
<class 'tuple'>
len(t)
7
id(s)
2769214707680
id(t)
2769213631824



#TYPE_CONVERSIONS

a = 20
a
20
float(a)
20.0
bool(a)
True
str(a)
'20'
complex(a)
(20+0j)
f=13.4
int(f)
13
f
13.4
comple(f)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    comple(f)
NameError: name 'comple' is not defined. Did you mean: 'compile'?
complex(f)
(13.4+0j)

str(f)
'13.4'
c= 12+2J
int(c)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> str(c)
'(12+2j)'
>>> s = 'codegnan'
>>> a='234234'
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'codegnan'
>>> int(a)
234234
>>> 234234
234234
>>> float(a)
234234.0
>>> complex(s)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    complex(s)
ValueError: complex() arg is a malformed string
>>> complex(a)
(234234+0j)
>>> bool(s)
True
>>> bool(a)
True
>>> list(s)
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
>>> tuple(s)
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
>>> set(s)
{'o', 'n', 'g', 'a', 'e', 'c', 'd'}
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
