n1=input()
n=n1.split()
l1=len(n)
l=0
for i in range(0,l1):
    num=int(n[i])
    l=l+num
if(l%2==0):
    print("even")
else:
    print("odd")
