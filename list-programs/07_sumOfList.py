def sumOfListRecursion(lst, size):
    if size == 0:
        return 0
    else:
        return lst[size-1] + sumOfListRecursion(lst, size-1)


def sumOfList(lst):
    sum = 0
    for i in lst:
        sum = sum+i
    print(f"Sum using for loop: {sum}")

    start = 0
    end = len(lst)-1
    sum = 0
    while(start <= end):
        if start != end:
            sum = sum + lst[start] + lst[end]
        else:
            sum = sum + lst[start]
        start = start+1
        end = end-1
    print(f"Sum using while loop: {sum}")

    print(f"Sum using Recursion: {sumOfListRecursion(lst, len(lst))}")


if __name__ == "__main__":
    lst = [10, 12, 15, 16, 17, 23, 1, 2, 5, 25, 4]
    print(f"Sample List: {lst}")
    sumOfList(lst)