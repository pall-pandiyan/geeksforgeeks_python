def sort_list(lst1, lst2):
    zipped = zip(lst2, lst1)
    return [x for _,x in sorted(zipped)]


if __name__ == "__main__":
    lst1 = ['a', 'c', 'd', 'f', 'g', 'h', 'o', 'n', 'p', 'q', 'z']
    lst2 = [5,9,8,6,7,4,1,0,2,3,10]
    print(f"List 1: {lst1}")
    print(f"List 2: {lst2}")
    print(f"sorted list: {sort_list(lst1, lst2)}")


# Sample:

# List 1: ['a', 'c', 'd', 'f', 'g', 'h', 'o', 'n', 'p', 'q', 'z']
# List 2: [5, 9, 8, 6, 7, 4, 1, 0, 2, 3, 10]
# sorted list: ['n', 'o', 'p', 'q', 'h', 'a', 'f', 'g', 'd', 'c', 'z']