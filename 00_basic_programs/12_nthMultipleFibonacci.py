def nthMultipleFibonacci(k, n):
    a = 0
    b = 1
    i = 2
    while (True):
        c = a+b
        a = b
        b = c

        if b%k == 0:
            return n*i
        i = i+1


if __name__ == "__main__":
    k = int(input("Enter divider: ").strip())
    n = int(input("Enter multiplier: ").strip())
    print(f"{nthMultipleFibonacci(k, n)}")


# Sample:

# Enter divider: 2
# Enter multiplier: 3
# 9

# Enter divider: 4
# Enter multiplier: 5
# 30