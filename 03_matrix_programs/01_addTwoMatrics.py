def addTwoMatrics(lst1, lst2):
    if len(lst1) != len(lst2):
        print(f"We cannot add two matrics with different sizes!")

    result = []
    for i in range(len(lst1)):
        row = []
        for j in range(len(lst1[i])):
            row.append(lst1[i][j] + lst2[i][j])
        result.append(row)
    print(f"added using for loops: {result}")

    result = [list(map(sum, zip(*t))) for t in zip(lst1,lst2)]
    print(f"added using list comprehension: {result}")


if __name__ == "__main__":
    lst1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    lst2 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]   
    ]
    print(f"List 1: {lst1}")
    print(f"List 2: {lst2}")
    addTwoMatrics(lst1, lst2)


# Sample:

# List 1: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# List 2: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# added using for loops: [[2, 4, 6], [8, 10, 12], [14, 16, 18]]