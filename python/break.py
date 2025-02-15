#break
i = 1
while i <= 6:
    print(i)
    if i  == 3:
        break
    i += 1
print("end of the loop")

#continue
a  = 0
while a <= 5:
    if (a == 3):
        a += 1
        continue
    print(a)
    a += 1