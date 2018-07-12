k=int(input())
s=""
for i in range(1,6):
    p=k*i
    s1=str(p)
    if(s==""):
        s=s1
    else:
        s=s+" "+s1
print(s)
