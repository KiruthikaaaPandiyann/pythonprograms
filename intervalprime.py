k=input()
k1=k.split()
a=int(k1[0])
b=int(k1[1])
s=""
for i in range(a+1,b):
    num=i
    if(num>1):
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            n=str(num)
            if(s==""):
                s=n
            else:
                s=s+" "+n
print(s)
