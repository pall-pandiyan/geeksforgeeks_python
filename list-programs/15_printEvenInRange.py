def printEvens(start, stop, step):
    for i in range(start, stop+1, step):
        print(i, end=" ")
    print()


if __name__ == "__main__":
    start = int(input("Enter the start range: ").strip())
    stop = int(input("Enter the stop range: ").strip())
    step = int(input("Enter the step: ").strip())

    printEvens(start, stop, step)

# Sample:

# Enter the start range: 100
# Enter the stop range: 200
# Enter the step: 5
# 100 105 110 115 120 125 130 135 140 145 150 155 160 165 170 175 180 185 190 195 200