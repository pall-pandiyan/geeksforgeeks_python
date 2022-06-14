def copyList(lst):
    result = lst[:]
    print(f"copy using slicing: {result}")

    result = []
    result.extend(lst)
    print(f"copy using extend: {result}")

    result = []
    for ele in lst:
        result.append(ele)
    print(f"copy using append(): {result}")

    result = list(lst)
    print(f"copy using list(): {result}")

    result = lst.copy()
    print(f"copy using copy(): {result}")

    result = [x for x in lst]
    print(f"copy using list comprehension: {result}")


if __name__ == "__main__":
    lst = [10, 3, 5, 1, 6, 9, 20, 15]
    print(f"Sample List: {lst}")
    copyList(lst)


# Sample:

# Sample List: [10, 3, 5, 1, 6, 9, 20, 15]
# copy using slicing: [10, 3, 5, 1, 6, 9, 20, 15]
# copy using extend: [10, 3, 5, 1, 6, 9, 20, 15]
# copy using append(): [10, 3, 5, 1, 6, 9, 20, 15]
# copy using list(): [10, 3, 5, 1, 6, 9, 20, 15]
# copy using copy(): [10, 3, 5, 1, 6, 9, 20, 15]
# copy using list comprehension: [10, 3, 5, 1, 6, 9, 20, 15]