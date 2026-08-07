Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
b = 12.3
c = 'codegnan'
a
10
b
12.3
>>> c
'codegnan'
>>> print(a,b,c)
10 12.3 codegnan
>>> print('a =',a,'b = ',b,'c = ',c)
a = 10 b =  12.3 c =  codegnan
>>> print('a =',a,'b = ',b,'c = ',c,sep="")
a =10b = 12.3c = codegnan
>>> print('a =',a,'b = ',b,'c = ',c,sep="\n")
a =
10
b = 
12.3
c = 
codegnan
>>> print('a =',a,'b = ',b,'c = ',c,sep='\t')
a =	10	b = 	12.3	c = 	codegnan
>>> print('a =',a,'b = ',b,'c = ',c,sep='\t',end='\n\n')
a =	10	b = 	12.3	c = 	codegnan

>>> print('a =',a,'b = ',b,'c = ',c,sep='\t',end="@")
a =	10	b = 	12.3	c = 	codegnan@
>>> print(f'a={a} b={b} c={c}')
a=10 b=12.3 c=codegnan
>>> print('a=%d b=%f c=%s')
a=%d b=%f c=%s
>>> print(f'a={} b={} c={}'.format(a,b,c,))
SyntaxError: f-string: valid expression required before '}'
>>> print('a={} b={} c={}'.format(a,b,c,))
a=10 b=12.3 c=codegnan
>>> 
>>> 
>>> print('a={} b={} c={}'.format(a,b,c,))
a=10 b=12.3 c=codegnan
>>> print('a={} b={} c={}'.format(b,c,a,))
a=12.3 b=codegnan c=10
>>> print('a={0} b={1} c={2}'.format(a,b,c,))
a=10 b=12.3 c=codegnan
>>> KeyboardInterrupt
>>> print('a={2} b={1} c={0}'.format(a,b,c,))
a=codegnan b=12.3 c=10
