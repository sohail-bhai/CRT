def even_odd(n: int) -> str:
   if n % 2 == 0:
       if (2 <= n <= 5) or (n > 20):
           return "Not Weird"
       elif 6 <= n <= 20:
           return "Weird"
   else:
       return "Weird"


if __name__ == '__main__':
    n = int(input())
    print(even_odd(n))