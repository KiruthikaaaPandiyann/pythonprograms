s=input()
s1=s.split()
a=int(s1[0])
b=int(s1[1])
c=int(s1[2])
if(a>b and a>c):
    print(a)
elif(b>a and b>c):
    print(b)
else:
    print(c)
