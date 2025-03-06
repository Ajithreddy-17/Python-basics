a = [1, 2, 0, 4, 5, 0, 1, 0, 3, 0, 5]
temp = []

n = len(a)
for i in range(n):
    if a[i] != 0:
        temp.append(a[i])

print(temp)

m = len(temp)

# Copy non-zero elements back to 'a'
for i in range(m):
    a[i] = temp[i]
    
# Fill the rest with zeros
for i in range(m, n):
    a[i] = 0

print(a)


