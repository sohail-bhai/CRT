'''print(min([5, 3, 8, 1, 4]))
print(max([5, 3, 8, 1, 4]))
print(sum([5, 3, 8, 1, 4]))

import math
#print(dir(math))
print(math.factorial(5))
gcd and lcm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

print(gcd(48, 18))
print(lcm(48, 18))
print(math.gcd(48, 18))
print(math.lcm(48, 18))  

def check_perfect_Number(n):
    if n < 2:
        return False
    sum_of_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_of_divisors == n
'''