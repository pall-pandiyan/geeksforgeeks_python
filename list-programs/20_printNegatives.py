def printNegatives(start, end):
    if end>0:
        end=0
    result = list(range(start, end))
    print(f"negatives in range using range(): {result}")

    print(f"negatives in range using for loop:", end=" ")
    for i in range(start,end):
        print(i, end=" ")
    print()


if __name__ == "__main__":
    start = int(input("Enter the start range: ").strip())
    end = int(input("Enter the end range: ").strip())
    printNegatives(start, end)


# sample:

# Enter the start range: -3
# Enter the end range: 5
# negatives in range using range(): [-3, -2, -1]
# negatives in range using for loop: -3 -2 -1