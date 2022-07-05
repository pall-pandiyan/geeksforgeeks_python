import numpy as np

def matrics_multiply(a, b):
    c = []
    for i in range(len(a)):
        temp = []
        for j in range(len(b[0])):
            sum = 0
            for k in range(len(b)):
                sum = sum + (a[i][k]*b[k][j])
            temp.append(sum)
        c.append(temp)
    print(f"The multiplication matrics using for loop is {c}")

    c = np.dot(a,b)
    print(f"The multiplication matrics using numpy is {c}")


if __name__ == "__main__":
    A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]

    B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]

    print(f"The matrics A is {A}")
    print(f"The matrics B is {B}")
    matrics_multiply(A, B)


# Sample:

# The matrics A is [[12, 7, 3], [4, 5, 6], [7, 8, 9]]
# The matrics B is [[5, 8, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]
# The multiplication matrics using for loop is [[114, 160, 60, 27], [74, 97, 73, 14], [119, 157, 112, 23]]
# The multiplication matrics using numpy is [[114 160  60  27]
#  [ 74  97  73  14]
#  [119 157 112  23]]