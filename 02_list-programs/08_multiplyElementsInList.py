from numpy import prod as np_prod
from math import prod as m_prod
from functools import reduce

def multiplyList(lst):
    result = 1
    for i in lst:
        result = result * i
    print(f"Multiply using for loop: {result}")

    start = 0
    end = len(lst)-1
    result = 1
    while(start<=end):
        if start != end:
            result = result * lst[start] * lst[end]
        else:
            result = result * lst[start]
        start = start+1
        end = end-1
    print(f"Multiply using while loop: {result}")

    print(f"Multiply using numpy.prod(): {np_prod(lst)}")

    print(f"Multiply using reduce(): {reduce(lambda x,y: x*y, lst)}")

    print(f"Multiply using math.prod(): {m_prod(lst)}")


if __name__ == "__main__":
    lst = [ 1, 5, 3, 10, 7, 20, 15, 100, 30, 40, 50]
    print(f"Sample List: {lst}")
    multiplyList(lst)

# Sample:

# Sample List: [1, 5, 3, 10, 7, 20, 15, 100, 30, 40, 50]
# Multiply using for loop: 1890000000000
# Multiply using while loop: 1890000000000
# Multiply using numpy.prod(): 1890000000000
# Multiply using reduce(): 1890000000000
# Multiply using math.prod(): 1890000000000