def num_length(num):
    n = 0
    while(num != 0):
        n += 1
        num //= 10
    return n

def power(x, y):
    if y==0:
        return 1
    if y%2 == 0:
        return power(x, y//2) * power(x, y//2)
    else:
        return x * power(x, y//2) * power(x, y//2)

def isArmStrongNumber(num):
    n = num_length(num)
    count = 0
    temp = num

    while temp!=0:
        r = temp%10
        temp //= 10
        count += power(r, n)
    return (count == num)

if __name__=="__main__":
    num = int(input("Enter a number to check for ArmStrong Number: ").strip())
    if isArmStrongNumber(num):
        print(f"{num} is a ArmStrong Number!")
    else:
        print(f"{num} is not a ArmStrong Number!")


# sample:

# Enter a number to check for ArmStrong Number: 153
# 153 is a ArmStrong Number!

# Enter a number to check for ArmStrong Number: 1253
# 1253 is not a ArmStrong Number!

# Enter a number to check for ArmStrong Number: 1634
# 1634 is a ArmStrong Number!