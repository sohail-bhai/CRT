'''
arithmetic series : 
input : 1 2 
output : 1 3 5 7 9 11 13 15 17 19
a,d=map(int,input().split())
for i in range(10):
    print(a+i*d,end=" ")

geometric series :
input : 2 3
output : 2 6 18 54 162 486 1458 4374 13122 39366
a,r=map(int,input().split())
for i in range(10):
    print(a*(r**i),end=" ")
fibonacci series :
input : 5
output : 0 1 1 2 3 
n=int(input())
a=0
b=1
seq=[]
for i in range(n):
    seq.append(a)
    a,b=b,a+b
print(seq)

factorial single number from series :
input : 5
output : 120 
n=int(input())
fact=1
if n==0 or n==1:
    print(1)
if n<0:
    print("Invalid input no")
for i in range(1,n+1):
    fact*=i
print(fact)
'''
