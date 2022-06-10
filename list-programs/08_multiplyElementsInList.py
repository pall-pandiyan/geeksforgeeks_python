def multiplyList(lst):
    result = 1
    for i in lst:
        result = result * i
    print(f"Multiply using for loop: {result}")


if __name__ == "__main__":
    lst = [ 1, 5, 3, 10, 7, 20, 15, 100, 30, 40, 50]
    multiplyList(lst)