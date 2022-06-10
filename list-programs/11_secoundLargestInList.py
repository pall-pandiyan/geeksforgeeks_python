def secondLargest(lst):
    largest = lst[0] if lst[0]>lst[1] else lst[1]
    largest2 = lst[0] if lst[0]<lst[1] else lst[1]
    for i in lst:
        if i>largest:
            largest2 = largest
            largest = i
        elif i>largest2 and i != largest:
            largest2 = i
    print(f"Second Largest using for loop: {largest2}")

    lst.sort()
    print(f"Secound Largest using sort(): {lst[-2]}")


if __name__ == "__main__":
    lst = [12, 10, 3, 5, 7, 2, 9, 11]
    print(f"Sample List is {lst}")
    secondLargest(lst)

# Sample:

# Sample List is [12, 10, 3, 5, 7, 2, 9, 11]
# Second Largest using for loop: 11
# Secound Largest using sort(): 11