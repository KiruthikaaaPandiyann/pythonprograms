n=int(input())
s=input()
s1=s.split()
add=0
for i in s1:
    num=int(i)
    add=add+num
avg=add//n
print(avg)

