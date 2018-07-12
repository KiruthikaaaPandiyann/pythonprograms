n=int(input())
s=input()
s1=s.split()
l=[]
for i in s1:
    a=int(i)
    l.append(a)
k=sorted(l)
mid=n//2
print(k[mid])
