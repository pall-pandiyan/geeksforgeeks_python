from math import sqrt, pow

def fibonacciFormula(n):
    sqrtOfFive = sqrt(5)
    result = (pow(1+sqrtOfFive, n) - pow(1-sqrtOfFive, n)) / (pow(2, n) * sqrtOfFive)
    return int(result)

if __name__ == "__main__":
    n = int(input("Enter a number: ").strip())
    if n<0:
        print(f"Error! {n} is not a positive value.")
    else:
        print(f"{fibonacciFormula(n)} is {n}th Fibonacci!")


# Sample:

# Enter a number: 12
# 144 is 12th Fibonacci!

# Enter a number: 10
# 55 is 10th Fibonacci!

# Enter a number: 11
# 89 is 11th Fibonacci