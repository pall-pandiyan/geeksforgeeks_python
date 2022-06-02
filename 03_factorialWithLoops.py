def factorialWithLoops(n):
    fact = 1
    for i in range(2,n+1):
        fact *= i
    return fact

if __name__=="__main__":
    n = int(in)