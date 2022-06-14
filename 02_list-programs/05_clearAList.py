if __name__ == "__main__":
    lst = [5, 4, 3, 45, 15, 100, 125, 130]
    print("Sample List: ", lst)
    lst.clear()
    print("After clear(): ", lst)

    lst = [5, 4, 3, 45, 15, 100, 125, 130]
    lst = []
    print("After assigning []: ", lst)

    lst = [5, 4, 3, 45, 15, 100, 125, 130]
    lst *= 0
    print("After *=0: ", lst)

    lst = [5, 4, 3, 45, 15, 100, 125, 130]
    del lst[:]
    print("After del: ", lst)


# Sample:

# Sample List:  [5, 4, 3, 45, 15, 100, 125, 130]
# After clear():  []
# After assigning []:  []
# After *=0:  []
# After del:  []