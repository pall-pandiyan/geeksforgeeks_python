def printEven(lst):
    result = []
    for i in lst:
        if i%2 == 0:
            result.append(i)
    print(f"using for loop: {result}")

    start = 0
    result = []
    while start<len(lst):
        i = lst[start]
        if i%2 == 0:
            result.append(i)
        start = start+1
    print(f"using while loop: {result}")


if __name__ == "__main__":
    lst = [2,10,15,1,3,6,20,100,14]
    print(f"sample list: {lst}")
    printEven(lst)

# Sample:

# sample list: [2, 10, 15, 1, 3, 6, 20, 100, 14]
# using for loop: [2, 10, 6, 20, 100, 14]
# using while loop: [2, 10, 6, 20, 100, 14]