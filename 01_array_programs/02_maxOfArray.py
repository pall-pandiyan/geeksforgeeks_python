def maxOfArray(arr):
    maximum = 0
    for element in arr:
        if maximum < element:
            maximum = element
    return maximum


if __name__ == "__main__":
    arr = list(map(int, input("Enter a array of numbers: ").split()))
    print(f"Maximum of array is {maxOfArray(arr)}")


# Sample:

# Enter a array of numbers: 1 5 10 100 5 2
# Maximum of array is 100