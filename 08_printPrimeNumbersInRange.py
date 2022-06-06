import math

def printPrimeNumbersInRange(n):
    if n<2:
        return False

    # r = 2
    # while r*r <= n:
    #     if n%r == 0:
    #         return False
    #     r = r+1

    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False

    return True


if __name__ == "__main__":
    x = int(input("Enter start range: ").strip())
    y = int(input("Enter end range: ").strip())

    print(f"Prime Number within the range of {x} and {y}:")
    for n in range(x,y):
        if printPrimeNumbersInRange(n):
            print(f"{n}", end=" ")
    print()


# Sample:

# Enter start range: 1
# Enter end range: 7
# Prime Number within the range of 1 and 7:
# 2 3 5 