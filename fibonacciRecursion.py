def fibonacci(n):
    if n==1 or n==2:
        return n-1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
if __name__ == "__main__":
    n = int(input("Enter a number: ").strip())
    print(f"Fibonacci Number of {n} is {fibonacci(n)}")


# Sample:

# Enter a number: 5
# Fibonacci Number of 5 is 3

# Enter a number: 10
# Fibonacci Number of 10 is 34