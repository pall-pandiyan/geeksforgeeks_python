def matrics_multiply(a, b):
    c = []
    for i in range(len(a)):
        temp = 0
        tempList = []
        for j in range(len(b[0])):
            temp = temp + (a[i][j] * b[j][i])
        tempList.append(temp)
    return c


if __name__ == "__main__":
    A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]

    B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]

    C = matrics_multiply(A,B)
    print(f"The matrics A is {A}")
    print(f"The matrics B is {B}")
    print(f"The multiplication matrics is {C}")


# Sample:

