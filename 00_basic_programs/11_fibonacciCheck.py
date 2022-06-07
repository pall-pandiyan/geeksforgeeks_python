def fibonacciCheck(n):
    a = 0
    b = 1
    while b<n:
        temp = a+b
        a = b
        b = temp
    
    return b==n

if __name__ == "__main__":
    n = int(input("Enter a number: ").strip())
    if fibonacciCheck(n):
        print(f"{n} is a Fibonacci Number!")
    else:
        print(f"{n} is not a Fibonacci Number!")


# Sample:

# Enter a number: 8
# 8 is a Fibonacci Number!

# Enter a number: 12
# 12 is not a Fibonacci Number!