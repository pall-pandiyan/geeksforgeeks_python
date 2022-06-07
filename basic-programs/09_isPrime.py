from math import sqrt

def isPrime(n):
    if n<2:
        return False

    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False

    return True


if __name__ == "__main__":
    n = int(input("Enter a number: ").strip())
    if isPrime(n):
        print(f"{n} is Prime Number!")
    else:
        print(f"{n} is not Prime Number!")


# Sample:

# Enter a number: 1
# 1 is not Prime Number!

# Enter a number: 2
# 2 is Prime Number!

# Enter a number: 3
# 3 is Prime Number!

# Enter a number: 5
# 5 is Prime Number!

# Enter a number: 6
# 6 is not Prime Number!

# Enter a number: 7
# 7 is Prime Number!