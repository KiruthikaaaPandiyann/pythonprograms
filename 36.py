l=input()
x=len(l)
c=0
for i in range(0,x):
    num=l[i]
    v=ord(num)
    if(v>=33 and v<=47):
        c=c+1
    if(v>=58 and v<=64):
        c=c+1
    if(v>=91 and v<=96):
        c=c+1
    if(v>=123 and v<=127):
        c=c+1
print(c)
