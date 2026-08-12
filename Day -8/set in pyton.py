Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
t = ()
t = tuple()
type(t)
<class 'tuple'>
t = (1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t = (1)
t
1
t = (1,)
t
(1,)
t = (1,1,1,1)
t
(1, 1, 1, 1)
t = (1,23.4,"str",[1,23],(1,2,3),{1,2,3},{1:1,2:2,3:3},True)
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}, True)
type(t)
<class 'tuple'>
()
()
(1,2,3)+(4,5,6)
(1, 2, 3, 4, 5, 6)
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}, True)
t[0]
1
t[-1]
True
t[3:7]
([1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3})
t[::-1]
(True, {1: 1, 2: 2, 3: 3}, {1, 2, 3}, (1, 2, 3), [1, 23], 'str', 23.4, 1)
t[-1:-3:-1]
(True, {1: 1, 2: 2, 3: 3})
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}, True)
23.4 in t
True
'str' in t
True
bool in t
False
t = (34,65234,6532,12,234,543)
t
(34, 65234, 6532, 12, 234, 543)
t.sorted()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    t.sorted()
AttributeError: 'tuple' object has no attribute 'sorted'
sorted(t)
[12, 34, 234, 543, 6532, 65234]
max(t)
65234
min(t)
12
len(t)
6
t.count(2)
0
t.count(12)
1
t= (1,2,3)
a,b,c = t
a
1
b
2
c
3
t = (1,2,3,[1,2,3,4],5)
t
(1, 2, 3, [1, 2, 3, 4], 5)
t.append[5]
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    t.append[5]
AttributeError: 'tuple' object has no attribute 'append'
t[4].append(5)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    t[4].append(5)
AttributeError: 'int' object has no attribute 'append'
t = (34,65234,6532,12,234,543)
t
(34, 65234, 6532, 12, 234, 543)
t.index(12)
3
all((1,2,3))
True
any((1,2,3,00,0))
True
t = (1,2,3,4,[1,2,3],5)
t
(1, 2, 3, 4, [1, 2, 3], 5)
t[4]
[1, 2, 3]
t[4].append(5)
t
(1, 2, 3, 4, [1, 2, 3, 5], 5)
t = (1,2,3,4,5)
sum(t)
15
(1, 2, 3, 4, [1, 2, 3, 5], 5)
(1, 2, 3, 4, [1, 2, 3, 5], 5)

s = {}
type(s)
<class 'dict'>
s = set()
type(s)
<class 'set'>
s = {1,2,3,4,5,6,1231243,124,2345,312}s
SyntaxError: invalid syntax
s
set()
s = {1,2,3,4,5,6,12,34,45,56,78,89,90,12345,765432,}
s = {1,2,3,4,5,6,12,34,45,56,78,89,90,12345,765432}
s
{89, 1, 2, 3, 4, 5, 6, 34, 765432, 12, 45, 78, 56, 12345, 90}
s = {1,1,1,1,1,1}
s
{1}
s = set()
s.add(1)
s.add(23.4)
s.add("str")
s
{1, 'str', 23.4}
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add(False)
s
{False, 1, 'str', 23.4}



3

3
3
#SET

a = {1,2,3,4,5,}
a = {1,2,3,4,5,}
a = {1,2,3,4,5}
b = {3,5,7,8,9}
2 in a
True
10 not in a
True
a|b
{1, 2, 3, 4, 5, 7, 8, 9}
a&b
{3, 5}
a - b
{1, 2, 4}
b-a
{8, 9, 7}
a ^ b
{1, 2, 4, 7, 8, 9}
a
{1, 2, 3, 4, 5}
{1}<=a
True
{1,2,3}<=a
True
{1,4,5,2}
{1, 2, 4, 5}
{1,4,5,2}<=a
True
{1,7,8}<=a
False
a>={1,2,3}
True
a>={68,9,}
False
m={1,2,3}
n={4,5,6}
n.disjoint(m)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    n.disjoint(m)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
n.isdisjoint(m)
True
a.isdisjoint(b)
False
a
{1, 2, 3, 4, 5}
a={3,4,2,454,23,45,23,45,23}
a
{2, 3, 4, 454, 23, 45}
max(a)
454
min(a)
2
len(a)
6
a.index(2)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    a.index(2)
AttributeError: 'set' object has no attribute 'index'
a.count(1)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    a.count(1)
AttributeError: 'set' object has no attribute 'count'
all({1,1,23,43,13,1})
True
any({0,''})
False
any({0,'',(),True})
True
sum(a)
531
a
{2, 3, 4, 454, 23, 45}
a = {1,2,3}
b =a
b
{1, 2, 3}
a
{1, 2, 3}
sorted(a)
[1, 2, 3]
b.add(4)
b
{1, 2, 3, 4}
a
{1, 2, 3, 4}
>>> b
>>> c = a.copy()
>>> c
{1, 2, 3, 4}
>>> c.add(5)
>>> c
{1, 2, 3, 4, 5}
>>> a
{1, 2, 3, 4}
>>> a.update({4,5,6,})
>>> a
{1, 2, 3, 4, 5, 6}
>>> a.pop()
1
>>> a
{2, 3, 4, 5, 6}
>>> a.pop()
2
>>> a
{3, 4, 5, 6}
>>> a.remove(6)
>>> a
{3, 4, 5}
>>> a.remove(6)
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    a.remove(6)
KeyError: 6
>>> a.discard(30)
>>> 
>>> a
{3, 4, 5}
>>> a.clear()
>>> a
set()
>>> a
set()
>>> a = frozenset({1,2,3,4})
>>> a
frozenset({1, 2, 3, 4})
