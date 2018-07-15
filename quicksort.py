def partition(arr,low,high):
    i = ( low-1 )         
    pivot = arr[high]     
    for j in range(low , high):
        if   arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
l=int(input())
s=input()
s1=s.split()
a=[]
for i in range(0,l):
    num=int(s1[i])
    a.append(num)
quickSort(a,0,l-1)
string=""
for i in a:
    ss=str(i)
    if(string==""):
        string=ss
    else:
        string=string+" "+ss
print(string)
