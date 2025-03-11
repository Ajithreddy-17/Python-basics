a = [1, 2, 3, 3, 5, 5, 5, 6]
b = [1, 3, 4, 5, 5, 7, 8]
intersection = []
n1 = len(a)
n2 = len(b)
i = 0
j = 0

while i < n1 and j < n2:
    if a[i] < b[j]:  # Move 'i' forward if a[i] is smaller
        i += 1
    elif a[i] > b[j]:  # Move 'j' forward if b[j] is smaller
        j += 1
    else:  # a[i] == b[j], so add to intersection
        if not intersection or intersection[-1] != a[i]:  # Avoid duplicates
            intersection.append(a[i])
        i += 1
        j += 1

print("Intersection:", intersection)

    


