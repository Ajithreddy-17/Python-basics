a=[1,2,3,4,5,6,7]
d=3
temp=[1,2,3]
n=len(a)
k=n-d
count =0
for i in range(d,n):#
    a[i-d] = a[i]
for j in range(k,n):
    count += 0
    a[j] = temp[count]
    count += 1
print(a)
    
