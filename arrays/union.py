a = [1, 1, 2, 3, 3, 4, 5]  # i
b = [1, 2, 4, 5, 6, 7, 8]  # j
union = []
n1 = len(a)
n2 = len(b)
i = 0
j = 0

while i < n1 and j < n2:
    if a[i] < b[j]:
        if not union or union[-1] != a[i]:  # Avoid duplicates
            union.append(a[i])
        i += 1
    elif a[i] > b[j]:
        if not union or union[-1] != b[j]:  # Avoid duplicates
            union.append(b[j])
        j += 1
    else:  # a[i] == b[j]
        if not union or union[-1] != a[i]:  # Avoid duplicates
            union.append(a[i])
        i += 1
        j += 1

# Add remaining elements from a
while i < n1:
    if union[-1] != a[i]:
        union.append(a[i])
    i += 1

# Add remaining elements from b
while j < n2:
    if union[-1] != b[j]:
        union.append(b[j])
    j += 1

print("Union:", union)



