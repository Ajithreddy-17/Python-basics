#question1
n=5
for i in range(n):
    if i%2 == 0:
     start = 1
    else:
       start = 0
    for j in range(i+1):
        print(start,end=" ")
        start=1-start
    print()
"""
1 
0 1 
1 0 1
0 1 0 1
1 0 1 0 1
"""
#question2
n=5
space=2*(n-1)
for i in range(n):
    for j in range(i):
     #numbers
     print(j+1,end=" ")
    for j in range(space):
       #space
       print(" ",end=" ")  
    for j in range(i,0,-1):
       #numbers
       print(j,end=" ")
    print()
    space -= 2
"""
1             1
1 2         2 1
1 2 3     3 2 1
1 2 3 4 4 3 2 1
"""
#question3
n=5
num=1
for i in range(n):
    for j in range(i):
      print(num,end=" ")
      num += 1
    print()
"""
1
2 3
4 5 6
7 8 9 10
"""
    
       
      
    
   