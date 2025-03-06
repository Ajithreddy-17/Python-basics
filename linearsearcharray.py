a = [1, 2, 3, 4, 5, 6]
num = 3
n = len(a)

flag = True

for i in range(n):
    if a[i] == num:
        flag = False
        break  # Only break if the element is found

if flag:
    print("not found")
else:
    print("found")

