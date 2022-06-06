fib = [0, 1]

def fibonacciDynamic(n):
    if n <= len(fib):
        return fib[n-1]
    else:
        temp = fibonacciDynamic(n-1) + fibonacciDynamic(n-2)
        fib.append(temp)
        return temp

if __name__ == "__main__":
    n = int(input("Enter a number: ").strip())
    if n < 0:
        print(f"Enter a positive value!")
    else:
        print(f"Fibonacci of {n} is {fibonacciDynamic(n)}")


# Sample:

# Enter a number: 5
# Fibonacci of 5 is 3

# Enter a number: 10
# Fibonacci of 10 is 34