def cumulativeSum(lst):
    result = []
    for i in range(len(lst)):
        result.append(sum(lst[:i+1]))
    print(f"sum list using sum(): {result}")

    result = []
    temp = 0
    for i in range(len(lst)):
        temp += lst[i]
        result.append(temp)
    print(f"sum list using for loop: {result}")


if __name__ == "__main__":
    lst = [10,2,5,20,1,25,100,52,27]
    print(f"Sample List: {lst}")
    cumulativeSum(lst)


# Sample:

# Sample List: [10, 2, 5, 20, 1, 25, 100, 52, 27]
# sum list using sum(): [10, 12, 17, 37, 38, 63, 163, 215, 242]
# sum list using for loop: [10, 12, 17, 37, 38, 63, 163, 215, 242]