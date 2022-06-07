def sumOfArray(arr):
    result = 0
    for element in arr:
        result = result + element
    return result

if __name__ == "__main__":
    arr = list(map(int, input("Enter the array: ").split()))
    # print(f"Sum of Array: {sum(arr)}")
    print(f"Sum of given array is {sumOfArray(arr)}")


# Sample:

# Enter the array: 110 12 1 15 23 100 158
# Sum of given array is 419