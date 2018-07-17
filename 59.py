n=int(input())
l=[]
while(n):
    a=n%10
    l.append(a)
    n=n//10
print(len(l))
