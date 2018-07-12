k=int(input())  
s=0  
temp=k  
while(temp>0):  
   t= temp%10  
   s=s+t**3
   temp=temp//10  
if(k==s):  
   print("yes")  
else:  
   print("no") 
