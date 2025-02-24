#question1
n = 5
ch = 'A'

for i in range(n):
    for j in range(ord(ch), ord(ch) + i + 1):
        print(chr(j), end=" ")  # Convert ASCII value back to character
    print()  # New line after each row
    """
A 
A B 
A B C
A B C D
A B C D E
"""

#question2

n = 5
ch = 'A'

for i in range(n-1,-1,-1):
    for j in range(ord(ch), ord(ch) + i + 1):
        print(chr(j), end=" ")  # Convert ASCII value back to character
    print()  # New line after each row
"""
A B C D E
A B C D
A B C
A B
A
"""
n=5
ch="A"
for i in range(n):
    char =ord(ch)+i
    for j in range(i+1):
        print(chr(char),end=" ")
    print()
"""
A
B B
C C C
D D D D
E E E E E
"""
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    ch ="A"
    for j in range(2*i+1):
        print(ch,end=" ")
        ch = chr(ord(ch)+1)
    print()
    """

        A
      A B C
    A B C D E
  A B C D E F G
A B C D E F G H I
"""