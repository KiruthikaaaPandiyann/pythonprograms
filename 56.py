n=input()
f1=0
f2=0
l=len(n)
for i in range(0,l):
    aa=n[i]
    a=ord(aa)
    if((a>=65 and a<=90)or(a>=97 and a<=122)):
        f1=f1+1
    if(a>=48 and a<=57):
        f2=f2+1
if(f1!=0 and f2!=0):
    print("yes")
else:
    print("no")
