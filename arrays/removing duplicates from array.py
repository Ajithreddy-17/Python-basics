a=[1,1,2,2,3,3,3]
n = len(a)
i=0
for j in range(1,n):
    if a[j] != a[i]:
        i += 1
        a[i] = a[j]
print(a[:i+1])
 
    
