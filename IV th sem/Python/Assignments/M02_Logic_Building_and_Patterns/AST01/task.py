def count_digits(n: int) -> int:
    n=str(n)
    return len(n)

if __name__ == "__main__":
    n = int(input())
    print(count_digits(n))
