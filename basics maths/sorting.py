list=[1,36,28,39,22,7,29]
for i in range(len(list)-1):
    for j in range(len(list)-i-1):
     if list[j] > list[j+1]:#swap
        list[j],list[j+1] = list[j+1],list[j]
print("sorted list",list)