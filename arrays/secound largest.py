#secound largest
arr = [1,5,8,25,33,30,2]
largest = arr[0]
secound_largest = arr[-1]
n =len(arr)
for i in range(n):
    if arr[i] > largest:
        largest = arr[i]
for i in range(n):
    if (arr[i] > secound_largest) and (arr[i] != largest):
        secound_largest = arr[i]
print(secound_largest)



