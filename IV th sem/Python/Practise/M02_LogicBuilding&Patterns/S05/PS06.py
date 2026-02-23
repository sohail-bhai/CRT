'''
li=[1,2,3,4,5]
output: [1,4,9,16,25]
li=list(map(int,input().split()))
print(list(map(lambda x:x**2,li)))

print even numbers of list 
li=list(map(int,input().split()))
print(*list(filter(lambda x:x%2==0,li)))

input ['s','o','h','a','i','l']
output sohail
li=list(input().split())
print(''.join(li))

pyramid pattern
output:
   *
  * *  
 * * *
* * * *
n=int(input())
li=""
for i in range(n):
    li+=" "*(n-i-1)+"* "*(i+1)+"\n"
print(li)

print inverted pyramid pattern
output:
* * * *
 * * *
  * *
   *
n=int(input())
li=""
for i in range(n):
    li+=" "*(i)+"* "*(n-i)+"\n"
print(li)

diamond pattern
output:
   *
  * *
 * * *
  * *
   *
n=int(input())
li=""
for i in range(n):
    li+=" "*(n-i-1)+"* "*(i+1)+"\n"
for i in range(n-1):
    li+=" "*(i+1)+"* "*(n-i-1)+"\n"
print(li)

number pyramid pattern use 
output:
   1
  1 2
 1 2 3
1 2 3 4
'''
n=int(input())
li=""
for i in range(n):
    li+=" "*(n-i-1)+" ".join(str(x) for x in range(1,i+2))+"\n"
print(li)
