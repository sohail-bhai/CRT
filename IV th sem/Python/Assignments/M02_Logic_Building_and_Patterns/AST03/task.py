def sum_of_digits(n: int) -> int:
    n=str(n)
    sum=0
    for i in n:
        sum+=int(i)
    return sum

if __name__ == "__main__":
    n = int(input())
    print(sum_of_digits(n))
