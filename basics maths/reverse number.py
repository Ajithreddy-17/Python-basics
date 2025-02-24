#reverse a number
n=7789
reverse =0 
while n > 0:
    last_digit = n%10
    n=n//10
    reverse =(reverse*10)+last_digit
print(reverse)