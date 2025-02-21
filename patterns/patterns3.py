#question1
r=5
c=4
for i in range(r):
    for j in range(c):
        if i == 0 or i == 4 or j== 0 or j == c-1:
         print("*",end=" ")
        else:
           print(" ",end=" ")
    print()
"""
* * * * 
*     * 
*     *
*     *
* * * *
"""
#question2
r=5
c=15
for i in range(r):
    for j in range(c):
        if i == 0 or i == 4 or j== 0 or j == c-1:
         print("*",end=" ")
        else:
           print(" ",end=" ")
    print()
"""
* * * * * * * * * * * * * * *
*                           *
*                           *
*                           *
* * * * * * * * * * * * * * *
"""
#question3
n=5
for i in range(n,-1,-1):
    for j in range(i):
      print(" ",end=" ")
    for j in range(n):
       print("*",end=" ")
    print()
    """
         * * * * *
        * * * * *
      * * * * *
    * * * * *
  * * * *  
* * * * *
"""
#question4
n=5
for i in range(n):
    for j in range(i+1):
      print(" ",end=" ")
    for k in range(n):
       print("*",end=" ")
    print()
    """
* * * * *
  * * * * *
    * * * * *
      * * * * *
        * * * * *
          * * * * *
          """



