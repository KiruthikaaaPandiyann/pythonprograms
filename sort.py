n=int(input())
s=input()
s1=s.split()
l=[]
for i in s1:
    a=int(i)
    l.append(a)
k=sorted(l)
string=""
for i in k:
    q=str(i)
    if(string==""):
        string=q
    else:
        string=string+" "+q
print(string)
