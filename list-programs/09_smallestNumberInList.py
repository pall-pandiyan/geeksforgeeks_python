def smallest_in_list(lst):

    smallest = lst[0]
    for i in lst:
        if i < smallest:
            smallest = i
    print(f"Smallest using for loop: {smallest}")

    start = 0
    end = len(lst)-1
    smallest = 0
    while start<=end:
        if lst[start] < lst[end]:
            temp = lst[start]
        else:
            temp = lst[end]
        
        if temp < smallest:
            smallest = temp
        start = start+1
        end = end-1
    print(f"Smallest using while loop: {smallest}")

    lst.sort()
    print(f"Smallest using sort(): {lst[0]}")

    print(f"Smallest using min(): {min(lst)}")

if __name__ == "__main__":
    # lst = list(map(int, input("Enter the list: ").split()))
    lst = [1, 3, 2, 5, 10, 7, 20, 15, 4, -3, 0, -2]
    print(f"Sample list: {lst}")
    smallest_in_list(lst)

# Sample:

# Sample list: [1, 3, 2, 5, 10, 7, 20, 15, 4, -3, 0, -2]
# Smallest using for loop: -3
# Smallest using while loop: -3
# Smallest using sort(): -3
# Smallest using min(): -3