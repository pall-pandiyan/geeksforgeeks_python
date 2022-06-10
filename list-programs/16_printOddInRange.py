def printOdds(start, end):
    if start%2 == 0:
        start = start+1
    for i in range(start, end+1, 2):
        print(i, end=" ")
    print()


if __name__ == "__main__":
    start = int(input("Enter the start range: ").strip())
    end = int(input("Enter the end range: ").strip())
    printOdds(start, end)

# Sample:

# Enter the start range: 50
# Enter the end range: 72
# 51 53 55 57 59 61 63 65 67 69 71 