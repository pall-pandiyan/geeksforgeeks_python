def swap_two_pos(lst, pos1, pos2):
    lstCopy = lst.copy()
    lstCopy[pos1-1], lstCopy[pos2-1] = lstCopy[pos2-1], lstCopy[pos1-1]
    return lstCopy


if __name__ == "__main__":
    lst = list(map(int, input("Enter the list: ").split()))
    pos1 = int(input("Enter the pos-1: ").strip())
    pos2 = int(input("Enter the pos-2: ").strip())
    print(swap_two_pos(lst, pos1, pos2))


# Sample:

# Enter the list: 3 3 5 4 8 9 7 10
# Enter the pos-1: 3
# Enter the pos-2: 8
# [3, 3, 10, 4, 8, 9, 7, 5]