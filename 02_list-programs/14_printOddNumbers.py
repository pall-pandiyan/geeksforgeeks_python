def printOdd(lst):
    result = []
    for i in lst:
        if i%2 == 1:
            result.append(i)
    print(f"print odds using for loop: {result}")

    start=0
    result = []
    while(start<len(lst)):
        i = lst[start]
        if i%2 ==1:
            result.append(i)
        start = start+1
    print(f"print odds using while loop: {result}")

    result = [x for x in lst if x%2==1]
    print(f"print odds using list comprehention: {result}")

    result = list(filter(lambda x: x%2==1, lst))
    print(f"print odds using filter() and lambda(): {result}")

if __name__ == "__main__":
    lst = [2,10,15,1,3,6,20,100,14]
    print(f"sample list: {lst}")
    printOdd(lst)

# Sample:

# sample list: [2, 10, 15, 1, 3, 6, 20, 100, 14]
# print odds using for loop: [15, 1, 3]
# print odds using while loop: [15, 1, 3]
# print odds using list comprehention: [15, 1, 3]
# print odds using filter() and lambda(): [15, 1, 3]