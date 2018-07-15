l=input()
x=len(l)
c=0
for i in range(0,x):
    num=l[i]
    v=ord(num)
    if(v>=49 and v<=58):
        c=c+1
print(c)
