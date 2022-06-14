def remove_tuples(lst):
    result = []
    for ele in lst:
        if ele != ():
            result.append(ele)
    print(f"remove using for loop: {result}")

    result = [x for x in lst if x!=()]
    print(f"remove using list comprehenstion: {result}")

    result = list(filter(lambda x: x!=(), lst))
    print(f"remove using filter() and lambda(): {result}")

if __name__ == "__main__":
    lst = [2, 3, (), 4, (), 8, 9, (), 1, 5]
    print(f"Sample List: {lst}")
    remove_tuples(lst)

# Sample:

# Sample List: [2, 3, (), 4, (), 8, 9, (), 1, 5]
# remove using for loop: [2, 3, 4, 8, 9, 1, 5]
# remove using list comprehenstion: [2, 3, 4, 8, 9, 1, 5]
# remove using filter() and lambda(): [2, 3, 4, 8, 9, 1, 5]