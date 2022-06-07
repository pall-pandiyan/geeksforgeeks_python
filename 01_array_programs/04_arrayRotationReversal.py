def arrayReverse(arr, start, end):
    arrCopy = arr.copy()

    while(start < end):
        # temp = arrCopy[start]
        # arrCopy[start] = arrCopy[end]
        # arrCopy[end] = temp
        arrCopy[start], arrCopy[end] = arrCopy[end], arrCopy[start]

        start = start + 1
        end = end -1
    return arrCopy


def arrayRotate(arr, n, d):
    arrCopy = arr.copy()

    # first rotate the displacement
    arrCopy = arrayReverse(arrCopy, 0, d-1)

    # then rotate the remaining elements
    arrCopy = arrayReverse(arrCopy, d, n-1)

    # now reverse the whole array
    arrCopy = arrayReverse(arrCopy, 0, n-1)
    
    return arrCopy


if __name__ == "__main__":
    arr = list(map(int, input("Enter the array: ").split()))
    d = int(input("Enter the displacement: ").strip())
    n = len(arr)

    result = arrayRotate(arr, n, d)
    print(result)


# Sample:

# Enter the array: 10 12 15 18 22 23 29 32
# Enter the displacement: 3
# [18, 22, 23, 29, 32, 10, 12, 15]