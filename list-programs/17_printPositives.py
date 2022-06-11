def printPositives(lst):
    print(f"Sample list: {lst}")

    result = []
    for i in lst:
        if i>=0:
            result.append(i)
    print(f"positives using for loop: {result}")

    start = 0
    result = []
    while(start<len(lst)):
        if lst[start]>=0:
            result.append(lst[start])
        start = start+1

    print(f"positives using while loop: {result}")
    
    result = [x for x in lst if x>=0]
    print(f"positives using list comprehension: {result}")

    result = list(filter(lambda x: x>=0 , lst))
    print(f"positives using filter() and lambda(): {result}")


if __name__ == "__main__":
    # lst = list(map(int, input("Enter the list: ").split()))
    lst = [5, 3, 1, 5, 0, 1, -1, -2, -2, 5, 3, 6, 8, 99, 100, -1]
    printPositives(lst)

# Sample:

# Sample list: [5, 3, 1, 5, 0, 1, -1, -2, -2, 5, 3, 6, 8, 99, 100, -1]
# positives using for loop: [5, 3, 1, 5, 0, 1, 5, 3, 6, 8, 99, 100]
# positives using while loop: [5, 3, 1, 5, 0, 1, 5, 3, 6, 8, 99, 100]
# positives using list comprehension: [5, 3, 1, 5, 0, 1, 5, 3, 6, 8, 99, 100]
# positives using filter() and lambda(): [5, 3, 1, 5, 0, 1, 5, 3, 6, 8, 99, 100]