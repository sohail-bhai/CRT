'''
print all factors of a number
Sample input: 12
Sample output: 1 2 3 4 6 12

n=int(input())
for i in range(1,n//2+1):
    if n%i==0:
        print(i,end=" ")
print(n)

count no of factors of a number
Sample input: 12
Sample output: 6

n=int(input())
count=0
for i in range(1,n//2+1):
    if n%i==0:
        count+=1
print(count+1)

print prime if a number is prime or not
Sample input: 12
Sample output: Not prime

Sample input: 13
Sample output: Prime

n=int(input())
is_prime=True
if n<2:
    is_prime=False
else:
    for i in range(2,n//2+1):
        if n%i==0:
            is_prime=False
            break
if is_prime:
    print("Prime")
else:
    print("Not prime")


print all prime numbers in a given range
Sample input: 1 10
Sample output: 2 3 5 7

start,end=map(int,input().split())
for i in range(start,end+1):
    is_prime=True
    if i<2:
        is_prime=False
    else:
        for j in range(2,i//2+1):
            if i%j==0:
                is_prime=False
                break
    if is_prime:
        print(i,end=" ")
print factorial of a number
Sample input: 5
Sample output: 120

n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)



'''

