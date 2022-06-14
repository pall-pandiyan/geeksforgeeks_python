def removeEmptyList(lst):
    result = []
    for ele in lst:
        if ele != []:
            result.append(ele)
    print(f"removed using for loop: {result}")

    ind = 0
    result = []
    while ind<len(lst):
        ele = lst[ind]
        if ele != []:
            result.append(ele)
        ind = ind+1
    print(f"removed using while loop: {result}")

    result = [x for x in lst if x!=[]]
    print(f"removed using list comprehension: {result}")

    result = list(filter(lambda x: x!=[], lst))
    print(f"removed using filter() and lambda(): {result}")


if __name__ == "__main__":
    lst = [1,3,5,[],4,6,[],35,20,50,30,[],26]
    print(f"Sample List: {lst}")
    removeEmptyList(lst)


# Sample:

# Sample List: [1, 3, 5, [], 4, 6, [], 35, 20, 50, 30, [], 26]
# removed using for loop: [1, 3, 5, 4, 6, 35, 20, 50, 30, 26]
# removed using while loop: [1, 3, 5, 4, 6, 35, 20, 50, 30, 26]
# removed using list comprehension: [1, 3, 5, 4, 6, 35, 20, 50, 30, 26]
# removed using filter() and lambda(): [1, 3, 5, 4, 6, 35, 20, 50, 30, 26]