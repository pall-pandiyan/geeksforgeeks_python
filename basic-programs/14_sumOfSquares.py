def sumOfSquares(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + (i*i)
    return sum


if __name__ == "__main__":
    n = int(input("Enter a number: ").strip())
    print(f"{sumOfSquares(n)}")


# Sample:

# Enter a number: 4
# 30

# Enter a number: 5
# 55