n=int(input())
s=""
while(n):
    a=n%10
    if(s==""):
        s=str(a)
    else:
        s=s+" "+str(a)
    n=n//10
print(s[::-1])
