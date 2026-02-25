'''
print first n rows of pascal triangle
input n=5
output:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
n=int(input("Enter number of rows: "))
for i in range(n):
    c=1
    for j in range(i+1):
        print(c,end=" ")
        c=c*(i-j)//(j+1)
    print()


BUtterfly pattern
input n=4
output:
*       *
**     **
***   ***
*********
*********
***   ***
**     **
*       *
n=int(input("Enter number of rows: "))
n=2*n
for i in range(1,n+1):
    if i<=n//2:
        print("*"*i,end="")
        print(" "*(n-2*i),end="")
        print("*"*i)
    else:
        print("*"*(n-i+1),end="")
        print(" "*(2*i-n-2),end="")
        print("*"*(n-i+1))
'''