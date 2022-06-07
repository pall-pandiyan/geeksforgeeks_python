def isArmStrongNumber(n):
    strN = str(n)
    length = len(strN)
    result = 0
    for ch in strN:
        result += int(ch) ** length

    return result == n


if __name__=="__main__":
    n = int(input("Enter the number to check for ArmStrong Number: ").strip())
    if isArmStrongNumber(n):
        print(f"The Number {n} is ArmStrong Number!")
    else:
        print(f"The Number {n} is not ArmStrong Number!")

# sample:

# Enter the number to check for ArmStrong Number: 153
# The Number 153 is ArmStrong Number!

# Enter the number to check for ArmStrong Number: 1263
# The Number 1263 is not ArmStrong Number!

# Enter the number to check for ArmStrong Number: 1634
# The Number 1634 is ArmStrong Number!