def factorialWithRecursion(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        return n * factorialWithRecursion(n-1)

if __name__ == "__main__":
    n = int(input("Enter a number: ").strip())
    print(f"Factorial of {n} is {factorialWithRecursion(n)}")