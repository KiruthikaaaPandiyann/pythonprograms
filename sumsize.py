j=input()
j1=j.split()
n=int(j1[0])
k=int(j1[1])
l=input()
x=l.split()
s=0
for i in range(0,k):
    a=int(x[i])
    s=s+a
print(s)
