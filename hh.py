n=5
for i in range(n):
    for j in range(n):
        if i == j or i == n-j-1:
         print("*",end=" ")
        else:
           print(" ",end=" ")
    print()