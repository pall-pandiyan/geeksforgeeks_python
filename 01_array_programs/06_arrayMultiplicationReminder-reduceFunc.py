from functools import reduce

def arrayMultiplicationReminder(arr, n):
    multi = reduce(lambda x,y: x*y, arr)
    return multi%n

if __name__ == "__main__":
    arr = list(map(int, input("Enter the array: ").split()))
    n = int(input("Enter the key: ").strip())
    print(arrayMultiplicationReminder(arr, n))


# Sample:

# Enter the array: 100 10 5 25 35 14
# Enter the key: 11
# 9