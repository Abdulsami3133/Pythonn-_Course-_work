Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
l = []
l = list()
type(l)
<class 'list'>
l = [1,12.3,"str",True,[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3}.3+4j]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
l = [1,12.3,"str",True,[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3}.3+4j]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
l = [1,12.3,"str",True,[1,2,3],(1,2,3),{1,2,3}, {1:1,2:2,3:3},3+4j]
l = [1,12.3,"str",True,[1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},3+4j]
l
[1, 12.3, 'str', True, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}, (3+4j)]
a= [1,2,3]
b= [4,5,6]
a+b
[1, 2, 3, 4, 5, 6]
a*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
a = [234,423,54,23,43534]
a[0]
234
a[5]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a[5]
IndexError: list index out of range
a[3]
23
a = [567,76,13,433,134,234]
a
[567, 76, 13, 433, 134, 234]
a[1]
76
a[3]
433
a[1:4]
[76, 13, 433]
a[::-1]
[234, 134, 433, 13, 76, 567]
76 in a
True
8765 in a
False
13 not in a
False
max(a)
567
min(a)
13
len(a)
6
sorted(a)
[13, 76, 134, 234, 433, 567]
id(a)
1370786068864
a[0]
567
a[0] = 56
id(a)
1370786068864
a[3] = 43
a[3]
43
id(a)
1370786068864
a.append(50)
a
[56, 76, 13, 43, 134, 234, 50]
a.append(12)
a
[56, 76, 13, 43, 134, 234, 50, 12]
sorted(a)
[12, 13, 43, 50, 56, 76, 134, 234]
a.insert(2,66)
a
[56, 76, 66, 13, 43, 134, 234, 50, 12]
a.extend([1,2,3])
a
[56, 76, 66, 13, 43, 134, 234, 50, 12, 1, 2, 3]
a.pop()
3
a.pop(0)
56
a.pop(5)
234
a.pop(2)
13
a
[76, 66, 43, 134, 50, 12, 1, 2]
a.remove(66)
a
[76, 43, 134, 50, 12, 1, 2]
>>> del a[1]
>>> a
[76, 134, 50, 12, 1, 2]
>>> a.clear()
>>> a
[]
>>> a
[]
>>> a = [76, 134, 50, 12, 1, 2]
>>> a
[76, 134, 50, 12, 1, 2]
>>> del a[0:3]
>>> a
[12, 1, 2]
>>> a.index(2)
2
>>> a.count(1)
1
>>> a = [1,2,3,4]
>>> b=a
>>> b
[1, 2, 3, 4]
>>> b.append(7)
>>> b
[1, 2, 3, 4, 7]
>>> c = a.copy()
>>> c
[1, 2, 3, 4, 7]
>>> a
[1, 2, 3, 4, 7]
>>> any([1,'',False,[],(),{},set()])
True
>>> any([0,'',False,[],(),{},set()])
False
>>> a
[1, 2, 3, 4, 7]
>>> a.sort()
>>> a.reverse()
>>> a
[7, 4, 3, 2, 1]
