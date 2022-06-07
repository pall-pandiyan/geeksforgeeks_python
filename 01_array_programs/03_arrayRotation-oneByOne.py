def rotateOneByOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i+1]
    arr[n-1] = temp
    return arr


if __name__ == "__main__":
    n = int(input("Enter the length of array: ").strip())
    arr = list(map(int, input("Enter the array: ").split()))
    d = int(input("Enter the displacement: ").strip())

    result = []
    for _ in range(d):
        result = rotateOneByOne(arr, n)
    print(result)


# Sample:

# Enter the length of array: 7
# Enter the array: 1 2 3 4 5 6 7 
# Enter the displacement: 3
# [4, 5, 6, 7, 1, 2, 3]