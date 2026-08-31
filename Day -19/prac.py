import sys
s,d,f,a=sys.stdin.read().splitlines()
p=5000
p*=1.4 if s.lower()=='business' else 1.2 if 'premium' in s.lower() else 1
p*=0.9 if int(d)>30 else 1.25 if int(d)<7 else 1
p*=1.2 if f.lower()=='true' else 1
p*=0.85 if int(a)>=60 else 1
print(float(p))