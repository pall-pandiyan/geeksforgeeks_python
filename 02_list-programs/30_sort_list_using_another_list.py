def sort_list(lst1, lst2):
    zipped = zip(lst2, lst1)
    print("sorted using zip():", [x for _,x in sorted(zipped)])

    result = {lst1[i]:lst2[i] for i in range(len(lst2))}
    sorted_list = sorted(result.items(), key=lambda x: x[1])
    result = [x for x,_ in sorted_list]
    print(f"sorted using dict: {result}")


if __name__ == "__main__":
    lst1 = ['a', 'c', 'd', 'f', 'g', 'h', 'o', 'n', 'p', 'q', 'z']
    lst2 = [5,9,8,6,7,4,1,0,2,3,10]
    print(f"List 1: {lst1}")
    print(f"List 2: {lst2}")
    sort_list(lst1, lst2)



# Sample:

# List 1: ['a', 'c', 'd', 'f', 'g', 'h', 'o', 'n', 'p', 'q', 'z']
# List 2: [5, 9, 8, 6, 7, 4, 1, 0, 2, 3, 10]
# sorted using zip(): ['n', 'o', 'p', 'q', 'h', 'a', 'f', 'g', 'd', 'c', 'z']
# sorted using dict: ['n', 'o', 'p', 'q', 'h', 'a', 'f', 'g', 'd', 'c', 'z']