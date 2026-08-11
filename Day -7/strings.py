Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = '              Hello              World                 '
a = '              Hello              World                 '
a
'              Hello              World                 '
a.strip()
'Hello              World'
a.lstrip()
'Hello              World                 '
a.rstrip()
'              Hello              World'
s.replace(' ',"")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    s.replace(' ',"")
NameError: name 's' is not defined
a.replcae(' ',"")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.replcae(' ',"")
AttributeError: 'str' object has no attribute 'replcae'. Did you mean: 'replace'?
a.replcae(' ','')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a.replcae(' ','')
AttributeError: 'str' object has no attribute 'replcae'. Did you mean: 'replace'?
a.replace(' ',"")
'HelloWorld'

    

s = 'java-python-c-mysql-flask'
s
'java-python-c-mysql-flask'
s.split("-")
['java', 'python', 'c', 'mysql', 'flask']
s.split("-",2)
['java', 'python', 'c-mysql-flask']
s.rsplit("-",2)
['java-python-c', 'mysql', 'flask']
a = '''python'''
a
'python'
a = '''python
java
mysql
flask
'''
a
'python\njava\nmysql\nflask\n'
a.splitlines()
['python', 'java', 'mysql', 'flask']
a = ['python','java','C','mysql']
a
['python', 'java', 'C', 'mysql']
''.join(a)
'pythonjavaCmysql'
" ".join(a)
'python java C mysql'
', '.join(a)
'python, java, C, mysql'
'@ '.join(a)
'python@ java@ C@ mysql'
'>'.join(a)
'python>java>C>mysql'
'-'.join(('1','2','3'))
'1-2-3'
'-'.join({'1','2','3'})
'2-1-3'
a = 'string.py'
a.partition('.')
('string', '.', 'py')
a = 'string.py.java.png.txt'
a
'string.py.java.png.txt'
a.partition('.')
('string', '.', 'py.java.png.txt')
a.rpartition('.')
('string.py.java.png', '.', 'txt')
a = 'strings.png'
a
'strings.png'
a.startswith('str')
True
a.startswith('list')
False
a.endswith('ng')
True
a.endswith('png')
True
'python 13'.islower()
True
'python 13'.isupper()
False
'PYTHON#@$@#^@#$%@#$%@#$'.isupper()
True
'edhfakshdfbahjd89778465347'.isalpha()
False
'asdfasdfasdfadf34345'.isaplha()
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    'asdfasdfasdfadf34345'.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
>>> 'asdfasdfasdfadf34345'.isalpha()
False
>>> 'sasdasihaskjdfajdgfahhdfadfg'.isalnum()
True
>>> '3234234234'.isalnum()
True
>>> '          '.isspace()
True
>>> '         hello'.isspace()
False
>>> 'hlo wor'.istitle()
False
>>> 'Hlo Wor'.istitle()
True
>>> 'my_var'.isidentifier()
True
>>> 'my@var'.isidentifier()
False
>>> a
'strings.png'
>>> a.partition('.')
('strings', '.', 'png')
>>> '21342342'.isdecimal()
True
>>> 'asdfasdfasdf323423'.isdecimail()
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    'asdfasdfasdf323423'.isdecimail()
AttributeError: 'str' object has no attribute 'isdecimail'. Did you mean: 'isdecimal'?
>>> 'adfasdfadsasdfasdf3r3r34'.isdecimal()
False
>>> '0981237'.isdegit()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    '0981237'.isdegit()
AttributeError: 'str' object has no attribute 'isdegit'. Did you mean: 'isdigit'?
>>> '2345678'.isdigit()
True
