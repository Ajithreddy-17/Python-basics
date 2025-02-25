n=371
sum=0
dup = n
while(n>0):
    last_digit = n%10
    n=n//10
    sum =sum+(last_digit*last_digit*last_digit)
if sum == dup:
    print("armstrong number")
else:
    print("not a armstrong")

