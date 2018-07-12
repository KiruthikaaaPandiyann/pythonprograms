k=input()
k1=k.split()
a=int(k1[0])
b=int(k1[1])
s=""
for i in range(a+1,b):
    if(i%2==0):
        a=str(i)
        if(s==""):
            s=a
        else:
            s=s+" "+a
print(s)
