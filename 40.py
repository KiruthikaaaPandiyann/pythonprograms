x=int(input())
a=0
b=1
n=x-1
s=""
s=str(b)
while(n>0):
    c=a+b
    a=b
    b=c
    s=s+" "+str(c)
    n=n-1
print(s)
