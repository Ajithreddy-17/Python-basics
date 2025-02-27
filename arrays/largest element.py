arr = [1,5,8,25,33,30,2]
largest =arr[0]
n = len(arr)
for i in range(n):
    if arr[i]> largest:
        largest = arr[i]
print(largest)

#secound example
a = [1,5,8,25,33,30,2]
n= len(a)
for i in range(n-1):
    for j in range(n-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]

print(a[-1])

