#secound smallest
a=[13,2,4,87,44,10]
smallest = a[0]
secound_smallest = a[-1]
n = len(a)
for i in range(n):
    if a[i] < smallest:
        smallest = a[i]
    if (a[i] < secound_smallest) and (a[i] != smallest):
        secound_smallest = a[i]
print(secound_smallest)
