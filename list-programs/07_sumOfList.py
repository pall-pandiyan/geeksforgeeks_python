def sumOfListRecursion(lst, size):
    if size == 0:
        return 0
    else:
        return lst[size-1] + sumOfListRecursion(lst, size-1)


def sumOfList(lst):
    total = 0
    for i in lst:
        total = total+i
    print(f"Sum using for loop: {total}")

    start = 0
    end = len(lst)-1
    total = 0
    while(start <= end):
        if start != end:
            total = total + lst[start] + lst[end]
        else:
            total = total + lst[start]
        start = start+1
        end = end-1
    print(f"Sum using while loop: {total}")

    print(f"Sum using Recursion: {sumOfListRecursion(lst, len(lst))}")

    print(f"Sum using sum(): {sum(lst)}")


if __name__ == "__main__":
    lst = [10, 12, 15, 16, 17, 23, 1, 2, 5, 25, 4]
    print(f"Sample List: {lst}")
    sumOfList(lst)


# Sample:

# Sample List: [10, 12, 15, 16, 17, 23, 1, 2, 5, 25, 4]
# Sum using for loop: 130
# Sum using while loop: 130
# Sum using Recursion: 130
# Sum using sum(): 130