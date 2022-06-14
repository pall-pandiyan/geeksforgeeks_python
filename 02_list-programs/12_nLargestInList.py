def nLargest(lst, n):
    lst2 = list(set(lst))
    lst2.sort()
    if len(lst2) < n:
        print(f"the target ({n}) exceeded length of unique list!")
    else:
        print(f"n largest using sort(): {lst2[-n:]}")

    result = []
    for i in range(n):
        max = lst[0]

        for j in range(1,len(lst)):
            if lst[j] > max:
                max = lst[j]
        
        result.append(max)
        lst.remove(max)
    result.sort()
    print(f"n largest using for loop: {result}")

if __name__ == "__main__":
    lst = [1,5,3,2,10,4,12,9]
    n = 3
    print(f"Sample List: {lst}")
    nLargest(lst, n)

# Sample:

# Sample List: [1, 5, 3, 2, 10, 4, 12, 9]
# n largest using sort(): [9, 10, 12]
# n largest using for loop: [9, 10, 12]