def printNegatives(start, end):
    if end>0:
        end=0
    result = list(range(start, end))
    print(f"negatives in range using range(): {result}")

    print(f"negatives in range using for loop:", end=" ")
    for i in range(start,end):
        print(i, end=" ")
    print()

    print(f"negatives in range using while loop:", end=" ")
    i = start
    while i!=end:
        print(i, end=" ")
        i = i+1
    print()

if __name__ == "__main__":
    start = int(input("Enter the start range: ").strip())
    end = int(input("Enter the end range: ").strip())
    printNegatives(start, end)


# sample:

# Enter the start range: -18
# Enter the end range: 1
# negatives in range using range(): [-18, -17, -16, -15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
# negatives in range using for loop: -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 
# negatives in range using while loop: -18 -17 -16 -15 -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1