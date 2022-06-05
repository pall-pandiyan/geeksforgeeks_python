def isPerfectNumber(n):
    muls = []
    for i in range(1,(n//2)+1):
        if n%i == 0:
            muls.append(i)
    return sum(muls)==n

if __name__ == "__main__":
    n = int(input("Enter a Number: ").strip())
    if isPerfectNumber(n):
        print(f"{n} is Perfect Number!")
    else:
        print(f"{n} is not Perfect Number!")


# sample:

# Enter a Number: 5
# 5 is not Perfect Number!

# Enter a Number: 15
# 15 is not Perfect Number!

# Enter a Number: 6
# 6 is Perfect Number!