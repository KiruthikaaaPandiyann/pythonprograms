n=int(input())
s=input()
s1=s.split()
l=[]
string=""
for i in s1:
    num=int(i)
    l.append(num)
a=min(l)
b=max(l)
string=str(a)+" "+str(b)
print(string)

