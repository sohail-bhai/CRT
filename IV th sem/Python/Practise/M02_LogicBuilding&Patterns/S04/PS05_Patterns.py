'''
square pattern 
n=4
* * * *
* * * *
* * * *
* * * *
n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

right angle triangle pattern
n=4
*
* *
* * *
* * * *
n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

Hollow square pattern
n=4
* * * *
*     *
*     *
* * * *

n=int(input("Enter the number of rows: "))
for i in range(n):
    if i ==0 or i==n-1:
        print("* "*n)
    else:
        print("*"+" "*(2*n-3)+"*")
  
inverted triangle pattern
n=4
* * * *
* * *
* *
*   
n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()

number triangle pattern
n=4
1
1 2
1 2 3
1 2 3 4
n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
'''
         
