
#quetsion1
n=5
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()
"""* * * * * 
* * * * 
* * * 
* * 
* 
"""
#question2
n=5
for i in range(n,-1,-1):
    for j in range(i):
        print(j+1,end=" ")
    print()
"""1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
"""
#question3
n=5
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()
    """
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
"""
#question4
n=5
for i in range(n-1,-1,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()
    """
 * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 
          """