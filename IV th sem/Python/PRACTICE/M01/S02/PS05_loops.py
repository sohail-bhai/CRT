#while loop:
'''
print("Hello world!")
print("Hello world!")
print("Hello world!")
print("Hello world!")
print("Hello world!")

counter = 0
while counter < 5:
    print("Hello world!")
    counter += 1

'''

'''
Question:
Read two intergers start and stop variables.
Dispaly all the even numbers between start and stop(inclusive)
Input : 1   10
Output : 2 4 6 8 10

Solution:
start = int(input())
stop = int(input())
while start <= stop:
    if start % 2 == 0:
        print(start,end=" ")
    start += 1

start = int(input())
stop = int(input())
while start <= stop:
    if start % 3 == 0 and start % 5 == 0:
        print("FizzBuzz")
    elif start % 3 == 0:
        print("Fizz")
    elif start % 5 == 0:
        print("Buzz")
    else:
        print(start)
    start += 1

for i in range(5):
    print("Hello world!")

# Display n natural numbers in the same line using for loop
n = int(input())
#N natural numbers
for i in range(1,n+1,1):
    print(i,end=" ")
print()
#n natural numbers in reverse order
for i in range(n,0,-1):
    print(i,end=" ")
'''
li = [1,5,4,3,6,9,10]
for i in range(0,len(li),1):
    if li[i] % 2 == 0:
        print(li[i],end=" ")

for i in li:
    if i % 2 == 0:
        print(i,end=" ")