import numpy as np

def printChessboardPattern(n):
    """This function will print 2D array with alternative 0's and 1's like chessboard"""

    result = np.zeros((n,n), dtype=int)

    # fill with 1 the alternate rows and columns
    result[1::2, ::2] = 1
    result[::2, 1::2] = 1

    for i in range(n):
        for j in range(1,n):
            print(result[i][j], end=" ")
        print()

if __name__ == "__main__":
    n = int(input("Enter a number: ").strip())
    printChessboardPattern(n)

#  sample:

# Enter a number: 8
# 1 0 1 0 1 0 1 
# 0 1 0 1 0 1 0 
# 1 0 1 0 1 0 1 
# 0 1 0 1 0 1 0 
# 1 0 1 0 1 0 1 
# 0 1 0 1 0 1 0 
# 1 0 1 0 1 0 1 
# 0 1 0 1 0 1 0