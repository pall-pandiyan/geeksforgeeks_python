def nLargest(lst, n):
    lst2 = list(set(lst))
    lst2.sort()
    if len(lst2) < n:
        print(f"the target ({n}) exceeded length of unique list!")
    else:
        print(f"n largest is {lst2[-n:]}")


if __name__ == "__main__":
    lst = [1,5,3,2,10,4,12,9]
    n = 3
    print(f"Sample List: {lst}")
    nLargest(lst, n)

# Sample:

# Sample List: [1, 5, 3, 2, 10, 4, 12, 9]
# n largest is [9, 10, 12]