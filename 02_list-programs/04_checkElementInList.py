def checkElement(lst, target):
    # if target in lst:
    #     return True
    # else:
    #     return False

    #for element in lst:
    #     if target == element:
    #         return True
    # return False

    if lst.count(target)>0:
        return True
    return False

if __name__ == "__main__":
    lst = list(map(int, input("Enter the list: ").split()))
    target = int(input("Enter a target: ").strip())
    if checkElement(lst, target):
        print(f"The target {target} is found in the list!")
    else:
        print(f"The target {target} is not found!")


# Sample:

# Enter the list: 1 2 3 4 5 6 8 10 54 9 74 100 125 111
# Enter a target: 100
# The target 100 is found in the list!

# Enter the list: 1 2 3 4 5 6 8 10 54 9 74 100 125 111
# Enter a target: 55
# The target 55 is not found