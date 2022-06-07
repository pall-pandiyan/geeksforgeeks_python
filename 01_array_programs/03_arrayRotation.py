def rotateArray(arr, n, d):
    result = []
    for i in range(d,n):
        result.append(arr[i])
    
    for i in range(d):
        result.append(arr[i])
    
    return result


if __name__ == "__main__":
    n = int(input("Enter the length of Array: ").strip())
    arr = list(map(int, input("Enter the array: ").split()))
    d = int(input("Enter the displacement: ").strip())

    print(rotateArray(arr, n, d))


# Sample:

# Enter the length of Array: 7
# Enter the array: 1 2 3 4 5 6 7
# Enter the displacement: 3
# [4, 5, 6, 7, 1, 2, 3]