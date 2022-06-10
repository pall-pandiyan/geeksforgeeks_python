from numpy import prod

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

    print(f"Muliply using numpy.prod(): {prod(lst)}")


if __name__ == "__main__":
    lst = [ 1, 5, 3, 10, 7, 20, 15, 100, 30, 40, 50]
    multiplyList(lst)