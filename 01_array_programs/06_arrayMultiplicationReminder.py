def arrayMultiplicationReminder(arr, n):
    result = 1
    for element in arr:
        result = result * element
    return result % n


if __name__ == "__main__":
    arr = list(map(int, input("Enter the array: ").split()))
    n = int(input("Enter the multiplier: ").strip())

    print(arrayMultiplicationReminder(arr, n))


# Sample:

# Enter the array: 100 10 5 25 35 14
# Enter the multiplier: 11
# 9