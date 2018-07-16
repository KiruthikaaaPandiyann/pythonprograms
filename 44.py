s=int(input())
flag=0
for i in range(1,11):
    if(i==s):
        flag=1
        break
if(flag==1):
    print("yes")
else:
    print("no")
