if __name__ == "__main__":
    lst = [2,5,10,12,13,15,20,16,25,1,30]
    print(f"Sample List: {lst}")

    n = len(lst)
    for i in range((n+1)//2):
        adjI = n-1-i
        # temp = lst[i]
        # lst[i] = lst[adjI]
        # lst[adjI] = temp
        lst[i], lst[adjI] = lst[adjI], lst[i]
    print(f"Reverse using for loop: {lst}")

    start = 0
    end = n-1
    while(start<end):
        lst[start], lst[end] = lst[end], lst[start]
        start = start+1
        end = end-1
    print(f"Reverse using while loop: {lst}")

    lst.reverse()
    print(f"Reverse using reverse(): {lst}")

    lst = list(reversed(lst))
    print(f"Reverse using reversed(): {lst}")

    lst2 = []
    for i in lst:
        lst2.insert(0, i)
    lst = lst2.copy()
    print(f"Reverse using insert(): {lst2}")
    del lst2

    print(f"Reverse using slicing: {lst}")


# Sample:

# Sample List: [2, 5, 10, 12, 13, 15, 20, 16, 25, 1, 30]
# Reverse using for loop: [30, 1, 25, 16, 20, 15, 13, 12, 10, 5, 2]
# Reverse using while loop: [2, 5, 10, 12, 13, 15, 20, 16, 25, 1, 30]
# Reverse using reverse(): [30, 1, 25, 16, 20, 15, 13, 12, 10, 5, 2]
# Reverse using reversed(): [2, 5, 10, 12, 13, 15, 20, 16, 25, 1, 30]
# Reverse using insert(): [30, 1, 25, 16, 20, 15, 13, 12, 10, 5, 2]
# Reverse using slicing: [30, 1, 25, 16, 20, 15, 13, 12, 10, 5, 2]