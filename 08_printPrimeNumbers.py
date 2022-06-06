def isPrintPrimeNumbers(n):
    if n<2:
        return False
    r = 2
    while r*r <= n:
        if n%r == 0:
            return False
        r = r+1
    
    return True

if __name__ == "__main__":
    # num = int(input("Enter a number: ").strip())
    # if isPrintPrimeNumbers(num):
    #     print(f"{num} is Prime Number!")
    # else:
    #     print(f"{num} is NOT Prime Number!")

    print(f"Prime Numbers upto 100:")
    for num in range(100):
        if isPrintPrimeNumbers(num):
            print(f"{num}", end=" ")
    print()


# Sample:

# Prime Numbers upto 100:
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97