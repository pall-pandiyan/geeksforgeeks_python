def printNegatives(lst):
    result = []
    for i in lst:
        if i<0:
            result.append(i)
    print(f"negatives using for loop: {result}")

    start = 0
    result = []
    while(start<len(lst)):
        if lst[start] <0:
            result.append(lst[start])
        start = start+1
    print(f"negatives using while loop: {result}")

    result = [x for x in lst if x<0]
    print(f"negatives using list compresion: {result}")

    result = list(filter(lambda x: x<0, lst))
    print(f"negatives using filter() and lambda(): {result}")


if __name__ == "__main__":
    lst = [-1, -10, 0, 5, 11, 15, 16, 18, 20, -5, -4]
    print(f"Sample List: {lst}")
    printNegatives(lst)


# Sample:

# Sample List: [-1, -10, 0, 5, 11, 15, 16, 18, 20, -5, -4]
# negatives using for loop: [-1, -10, -5, -4]
# negatives using while loop: [-1, -10, -5, -4]
# negatives using list compresion: [-1, -10, -5, -4]
# negatives using filter() and lambda(): [-1, -10, -5, -4]