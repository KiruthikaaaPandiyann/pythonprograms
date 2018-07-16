s=int(input())
flag=0
for i in range(0,s):
    num=2**i
    if(num==s):
        flag=1
        break
if(flag==1):
    print("yes")
else:
    print("no")

