def isPerfectNumber(n):
    if n<2:
        return False
    sum = 1
    r = 2
    while r*r <= n:
        if n%r == 0:
            sum = sum+r+n/r
        r = r+1
    return sum == n

if __name__ == "__main__":
    # n = int(input("Enter a Number: ").strip())
    # if isPerfectNumber(n):
    #         print(f"{n} is Perfect Number!")
    # else:
    #     print(f"{n} is not Perfect Number!")

    for n in range(10000):
        if isPerfectNumber(n):
            print(f"{n} is Perfect Number!")


# sample:

# 6 is Perfect Number!
# 28 is Perfect Number!
# 496 is Perfect Number!
# 8128 is Perfect Number!