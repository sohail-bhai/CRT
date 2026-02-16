'''
check if a number ( given ) is strong number or not
input : 145
output : strong number
input : 123
output : not a strong number
n=int(input())
temp=n
sum=0
while temp>0:
    digit=temp%10
    fact=1
    for i in range(1,digit+1):
        fact*=i
    sum+=fact
    temp//=10
if sum==n:
    print("strong number")
else:
    print("not a strong number")

check if a number ( given ) is perfect number or not
input : 6
output : perfect number
input : 10
output : not a perfect number

n=int(input())
temp=n      
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print("perfect number")
else:
    print("not a perfect number")
    
'''