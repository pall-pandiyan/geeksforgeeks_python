def printPositives(start, end):
    if start<0:
        start=0
    result = list(range(start,end+1))
    print(f"positives on range using range(): {result}")

    print(f"positives on range using for loop:", end=" ")
    for i in range(start, end+1):
        print(i, end=" ")
    print()

    i = start
    print(f"positives on range using while loop:", end=" ")
    while(i!=end+1):
        print(i, end=" ")
        i = i+1
    print()


if __name__ == "__main__":
    start = int(input("Enter the start range: ").strip())
    end = int(input("Enter the end range: ").strip())
    printPositives(start, end)


# Sample:

# Enter the start range: 0
# Enter the end range: 5
# positives on range using range(): [0, 1, 2, 3, 4, 5]
# positives on range using for loop: 0 1 2 3 4 5 
# positives on range using while loop: 0 1 2 3 4 5 