'''
Print no of digits in a number
Sample input:1234
sample output: 4

Sample input: 56789
sample output: 5
n=int(input())
count=0
while n>0:
    count+=1
    n//=10
print(count)
'''

'''
PRint the sum of digits in a number
Sample input: 1234  
Sample output: 10

Sample input: 56789
Sample output: 35
n=int(input())
sum=0
while n>0:
    sum+=n%10
    n//=10
print(sum)
'''
'''
Print even digits in a number
Sample input: 1234
Sample output: 2 4
Sample input: 56789
Sample output: 6 8
n=int(input())
s=""
while n>0:
    digit=n%10
    if digit%2==0:
        s+=str(digit)+" "
    n//=10
print(s[::-1])
'''

'''
print reverse of a number
Sample input: 1234
Sample output: 4321

Sample input: 56789
Sample output: 98765
n=int(input())
rev=0
while n>0:
    rev=rev*10+n%10
    n//=10
print(rev)

'''

'''
if given number is palindrome or not
Sample input: 1234
Sample output: Not a palindrome
Sample input: 1221
Sample output: palindrome

def reverse(n):
    rev=0
    while n>0:
        rev=rev*10+n%10
        n//=10
    return rev
n=int(input())
if n==reverse(n):
    print("Palindrome")
else:
    print("Not a palindrome")
'''

'''
check if a number is armstrong or not
Sample input: 153
Sample output: armstrong
Sample input: 123
Sample output: not armstrong
n=int(input())
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if sum==n:
    print("Armstrong")
else:    
    print("Not Armstrong")

count even and odd digits in a number
Sample input: 1234
Sample output: Even digits: 2, Odd digits: 2
Sample input: 56789
Sample output: Even digits: 1, Odd digits: 4
n=int(input())
even_count=0
odd_count=0
while n>0:
    digit=n%10
    if digit%2==0:
        even_count+=1
    else:
        odd_count+=1
    n//=10
print(f"Even digits: {even_count}, Odd digits: {odd_count}")


find largest and smallest digit in a number
Sample input: 1234
Sample output: Largest digit: 4, Smallest digit: 1
Sample input: 56789
Sample output: Largest digit: 9, Smallest digit: 5
n=int(input())
largest=0
smallest=9
while n>0:
    digit=n%10
    if digit>largest:
        largest=digit
    if digit<smallest:
        smallest=digit
    n//=10
print(f"Largest digit: {largest}, Smallest digit: {smallest}")

count zero digits in a number
Sample input: 102030
Sample output: Number of zero digits: 3
Sample input: 12345
Sample output: Number of zero digits: 0
n=int(input())
zero_count=0
while n>0:
    digit=n%10
    if digit==0:
        zero_count+=1
    n//=10
print(f"Number of zero digits: {zero_count}")

find digital root of a number
Sample input: 16
Sample output: Digital root: 7
Sample input: 942
Sample output: Digital root: 6
n=int(input())
while n>=10:
    sum=0
    while n>0:
        sum+=n%10
        n//=10
    n=sum
print(f"Digital root: {n}")

'''
