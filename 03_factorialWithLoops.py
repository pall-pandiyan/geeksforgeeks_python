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