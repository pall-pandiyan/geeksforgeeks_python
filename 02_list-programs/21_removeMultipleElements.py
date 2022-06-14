def removeMultiples(lst):
    l = []
    for ele in lst:
        if ele%2 == 1:
            l.append(ele)
    print(f"removed using for loop: {l}")

    l = []
    start = 0
    while(start<len(lst)):
        ele = lst[start]
        if ele%2 == 1:
            l.append(ele)
        start = start+1
    print(f"removed using while loop: {l}")

    result = [x for x in lst if x%2==1]
    print(f"remove using list comprehension: {result}")

    reult = list(filter(lambda x: x%2==1, lst))
    print(f"remove using filter() and lambda(): {result}")

if __name__ == "__main__":
    lst = [1,3,5,10,4,6,25,35,20,50,30,100,26]
    print(f"Sample List: {lst}")
    removeMultiples(lst)


# Sample:

# Sample List: [1, 3, 5, 10, 4, 6, 25, 35, 20, 50, 30, 100, 26]
# removed using for loop: [1, 3, 5, 25, 35]
# removed using while loop: [1, 3, 5, 25, 35]
# remove using list comprehension: [1, 3, 5, 25, 35]
# remove using filter() and lambda(): [1, 3, 5, 25, 35]