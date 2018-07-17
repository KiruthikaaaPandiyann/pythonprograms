n=input()
s=input()
s1=s.split()
n1=n.split()
a=int(n1[0])
b=int(n1[1])
l=[]
for i in range(0,a):
    num=int(s1[i])
    l.append(num)
if(b in l):
    print("yes")
else:
    print("no")
