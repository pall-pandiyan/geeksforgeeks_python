from math import sqrt

# A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square
def perfectSqrt(n):
    sq = int(sqrt(n))
    return sq * sq == n


def fibonacciCheckFormula(n):
    if perfectSqrt(5*n*n + 4) or perfectSqrt(5*n*n - 4):
        return True
    else:
        return False


if __name__ == "__main__":
    n = int(input("Enter a number: ").strip())
    if fibonacciCheckFormula(n):
        print(f"{n} is a Fibonacci Number!")
    else:
        print(f"{n} is not a Fibonacci Number!")


# Sample:

# Enter a number: 8
# 8 is a Fibonacci Number!

# Enter a number: 34
# 34 is a Fibonacci Number!

# Enter a number: 35
# 35 is not a Fibonacci Number!