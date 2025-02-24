n = 7789
count=0
while n > 0:
    last_digit = n % 10 
    count +=1
    n = n // 10  
print(count)
    
