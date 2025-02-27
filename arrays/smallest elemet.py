#smallest element
arr = [9,5,8,25,33,30,2]
smallest = arr[0]
n = len(arr)
for i in range(n):
    if arr[i] < smallest:
        smallest = arr[i]
print(smallest)