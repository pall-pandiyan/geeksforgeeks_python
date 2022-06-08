def checkMonoArray(arr):
    moving_up = False
    moving_down = False
    n = len(arr)

    for i in range(n-1):
        if (moving_up and arr[i]>arr[i+1]) or (moving_down and arr[i]<arr[i+1]):
            return False
        else:
            if arr[i] > arr[i+1]:
                moving_down = True
                moving_up = False
            elif arr[i] < arr[i+1]:
                moving_up = True
                moving_down = False
            else:
                moving_down = False
                moving_up = False
    return True

if __name__ == "__main__":
    arr = list(map(int, input("Enter a array: ").split()))
    if checkMonoArray(arr):
        print("The array is a monotone array.")
    else:
        print("The array is NOT a monotone array.")


# Sample:

# Enter a array: 3 5 6 7 9 10
# The array is a monotone array.

# Enter a array: 3 5 1 2 3
# The array is NOT a monotone array.