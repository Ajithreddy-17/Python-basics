#gcd or hcf
a=11
b=13
gcd =1
for i in range(1,min(a,b)+1):
    if (a % i == 0 and b & i == 0):
        gcd =i
print(gcd)


