def prod(val):
    result = 1
    for i in val:
        for j in i:
            result = result * j
    return result

if __name__ == "__main__":
    arr = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
    print(f"The matrix is {arr}")
    print(f"The product using for loop is {prod(arr)}")


# Sample:

# The matrix is [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
# The product using for loop is 1622880