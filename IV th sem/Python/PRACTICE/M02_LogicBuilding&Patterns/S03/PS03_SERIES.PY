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
input : 0 1
output : 0 1 1 2 3 5 8 13 21 34
a,b=map(int,input().split())
for i in range(10):
    print(a,end=" ")
    a,b=b,a+b
'''


