def get_length_of_list(lst):
    return len(lst)

if __name__ == "__main__":
    lst = list(map(int, input("Enter the list: ").split()))
    print(f"Length of the list is {get_length_of_list(lst)}")


# Sample:

# Enter the list: 1 2 3 4 5 6
# Length of the list is 6