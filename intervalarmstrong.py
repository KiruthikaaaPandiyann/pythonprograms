k=input()
k1=k.split()
a=int(k1[0])
b=int(k1[1])
z=""
for i in range(a+1,b):
    num=i
    s=0  
    temp=num 
    while(temp>0):  
       t= temp%10  
       s=s+t**3
       temp=temp//10  
    if(s==num):
        n=str(num)
        if(z==""):
            z=n
        else:
            z=z+" "+n
print(z)
