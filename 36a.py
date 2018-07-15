l=input()
x=len(l)
c=0
for i in range(0,x):
    num=l[i]
    v=ord(num)
    if((v>=33 and v<=47)or(v>=58 and v<=64)or(v>=91 and v<=96)or(v>=123 and v<=127)):
        c=c+1
print(c)
