n=input()
l=len(n)
flag=0
for i in range(0,l):
    num=int(n[i])
    if(num==1 or num==0):
        flag=flag+1
    else:
        flag=0
        break
if(flag>0):
    print("yes")
else:
    print("no")
