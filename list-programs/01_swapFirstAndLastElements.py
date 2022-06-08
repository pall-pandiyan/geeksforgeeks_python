def swap_first_and_last_elements(lst):
    lstCopy = lst.copy()
    n = len(lst)
    lstCopy[0], lstCopy[n-1] = lstCopy[n-1], lstCopy[0]
    return lstCopy

if __name__ == "__main__":
    lst = list(map(int, input("Enter the list: ").split()))
    result = swap_first_and_last_elements(lst)
    print(result)


# Sample:

# Enter the list: 1 2 3 4 5 6 7 10 12 22 50
# [50, 2, 3, 4, 5, 6, 7, 10, 12, 22, 1]