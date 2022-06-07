def factorialWithLoops(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact = 1
        for i in range(2,n+1):
            fact *= i
        return fact

if __name__=="__main__":
    n = int(input("Enter the number: "))
    print(f"Factorial of {n} is {factorialWithLoops(n)}")



# samples:

# Enter the number: 10
# Factorial of 10 is 3628800

# Enter the number: 0
# Factorial of 0 is 1

# Enter the number: 1
# Factorial of 1 is 1

# Enter the number: -10
# Factorial of -10 is 0