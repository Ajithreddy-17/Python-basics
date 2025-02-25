n=1331
reverse =0
dup = n 
while (n>0):
    last_digit = n%10
    n = n//10
    reverse = (reverse*10)+last_digit
print(reverse)
if dup == reverse :
    print("palindrome")
else:
    print("not")