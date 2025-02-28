a = [1,2,3,99,6,7]
n = len(a)
flag =  True
for i in range(n-1):
    if (a[i] > a[i+1]):
       flag = False
       break
if flag:
    print("sorted")
else:
    print("not sorted")



