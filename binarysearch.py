def binarysearch(a,fir,last,num):
    while fir<=last:
        mid = (fir + last) // 2
        if a[mid]==num:
           return mid
        elif a[mid]>num:
            last=mid-1
        elif a[mid]<num:
            fir=mid+1
        else:
            print("Element not found")
a=[]
l=int(input("Enter the range:"))
print("Enter the elements of array:")
for i in range(l):
    a.append(int(input()))
print("Enter the element you want to search")
num=(int(input()))
a.sort()
print(a)
fir=0
last=l-1
result = binarysearch(a, fir, last, num)
print("Element is at the position", result)



