def printNegatives(start, end):
    if end>0:
        end=0
    result = list(range(start, end))
    print(f"negatives in range using range(): {result}")


if __name__ == "__main__":
    start = int(input("Enter the start range: ").strip())
    end = int(input("Enter the end range: ").strip())
    printNegatives(start, end)


# sample:

# Enter the start range: -6
# Enter the end range: 6
# negatives in range using range(): [-6, -5, -4, -3, -2, -1]