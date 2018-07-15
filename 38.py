n=input()
n1=n.split()
a=int(n1[0])
b=int(n1[1])
a=a^b
b=a^b
a=a^b
s=""
s=str(a)+" "+str(b)
print(s)
