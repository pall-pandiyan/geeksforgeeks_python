def largestList(lst):
    largest = lst[0]
    for i in lst:
        if largest < i:
            largest = i
    print(f"Largest using for loop: {largest}")

    start = 1
    end = len(lst)-1
    largest = lst[0]
    while start<=end:
        if lst[start]>lst[end]:
            temp = lst[start]
        else:
            temp = lst[end]
        if temp > largest:
            largest = temp
        start = start+1
        end = end-1
    print(f"Largest using while loop: {largest}")

    print(f"Largest using max(): {max(lst)}")

    lst.sort()
    print(f"Largest using sort(): {lst[len(lst)-1]}")


if __name__ == "__main__":
    lst = [1,3,5,6,2,4,10,13,11,20]
    print(f"Sample List is {lst}")
    largestList(lst)


# Sample:

# Sample List is [1, 3, 5, 6, 2, 4, 10, 13, 11, 20]
# Largest using for loop: 20
# Largest using while loop: 20
# Largest using max(): 20
# Largest using sort(): 20