def fibonacciSpaceOptimized(n):
    a = 0
    b = 1

    for i in range(1, n):
        temp = a+b
        a = b
        b = temp
    return b


if __name__ == "__main__":
    n = int(input("Enter a number: ").strip())
    if n<0:
        print(f"Error! {n} is not a positive number!")
    else:
        print(f"{fibonacciSpaceOptimized(n)} is {n}th Fibonacci Number.")


# Sample:

# Enter a number:12
# 144 is 12th Fibonacci Number.