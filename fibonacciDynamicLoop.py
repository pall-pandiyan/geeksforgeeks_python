def fibonacciDynamicLoop(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fibonacciDynamicLoop(n-1) + fibonacciDynamicLoop(n-2))

    return fib[n-1]

if __name__ == "__main__":
    num = int(input("Enter a number: ").strip())
    if num<0:
        print(f"Error! Please enter a positive number!")
    else:
        print(f"Fibonacci of {num} is {fibonacciDynamicLoop(num)}")


# Sample:

# Enter a number: 10
# Fibonacci of 10 is 34

# Enter a number: 5
# Fibonacci of 5 is 3