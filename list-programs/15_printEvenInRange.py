def printEvens(start, stop):
    if start%2 == 1:
        start = start+1
    for i in range(start, stop+1, 2):
        print(i, end=" ")
    print()


if __name__ == "__main__":
    start = int(input("Enter the start range: ").strip())
    stop = int(input("Enter the stop range: ").strip())

    printEvens(start, stop)

# Sample:

# Enter the start range: 11
# Enter the stop range: 30
# 12 14 16 18 20 22 24 26 28 30 