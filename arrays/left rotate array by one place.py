a=[1,2,3,4,5]
temp =a[0]
n=len(a)
for i in range(1,n-1):
    a[i-1]=a[i]
a[n-1] = temp
print(a)
