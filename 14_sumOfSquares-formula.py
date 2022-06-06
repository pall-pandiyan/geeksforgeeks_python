def sumOfSquares(n):
    return (n*(n+1)*(2*n+1)) // 6


if __name__ == "__main__":
    n = int(input("Enter a number: ").strip())
    print(f"{sumOfSquares(n)}")


# Sample:

# Enter a number: 4
# 30

# Enter a number: 5
# 55