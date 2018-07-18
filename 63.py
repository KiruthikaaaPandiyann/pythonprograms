n1=input()
n=n1.split()
l1=len(n)
l=[]
for i in range(0,l1):
    num=int(n[i])
    l.append(num)
print(min(l))
