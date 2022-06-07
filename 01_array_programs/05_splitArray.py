def splitArray(arr, n, k):
    for i in range(k):
        temp = arr[0]
        for j in range(n-1):
            arr[j] = arr[j+1]
        arr[n-1] = temp
    return arr


if __name__ == "__main__":
    arr = list(map(int, input("Enter the array: ").split()))
    k = int(input("Enter the key: ").strip())
    n = len(arr)
    result = splitArray(arr, n, k)
    print(result)


# Sample:

# Enter the array: 15 12 13 15 7 8 748 958 54
# Enter the key: 4
# [7, 8, 748, 958, 54, 15, 12, 13, 15]