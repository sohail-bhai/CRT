from typing import List


def Collatz_Sequence(n: int)-> List:
   seq=[]
   while n!=1:
       seq.append(n)
       if n%2==0:
           n=n//2
       else:
           n=3*n+1
   seq.append(1)
   return seq
if __name__ == '__main__':
    n = int(input())
    print(Collatz_Sequence(n))