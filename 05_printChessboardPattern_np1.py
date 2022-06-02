import numpy as np

def printChessboardPattern(n):
    """This function will print 2D array with alternative 0's and 1's like chessboard"""

    result = np.zeros((n,n), dtype=int)
    for i in range(n):
        if i%2 == 0:
            result[i][0] = 1

        for j in range(1,n):
            if result[i][j-1] == 0:
                result[i][j]=1
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