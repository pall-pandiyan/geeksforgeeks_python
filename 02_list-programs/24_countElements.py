from collections import Counter

def count_elements(lst):
    l = set(lst)
    # print("count element using count(): ")
    result = {}
    for ele in l:
        # print(f"{ele}x{lst.count(ele)}")
        result[ele] = lst.count(ele)
    print(f"count using count(): {result}")

    result = {}
    for k in l:
        count = 0
        for v in lst:
            if v == k:
                count = count+1
        result[k] = count
    print(f"count using for loop: {result}")

    c = Counter(lst)
    result = {}
    for k in l:
        result[k] = c[k]
    print(f"count using Counter: {result}")


if __name__ == "__main__":
    lst = [1, 5, 9, 6, 3, 1, 5, 3, 1, 9]
    print(f"Sample List: {lst}")
    count_elements(lst)


# Sample:

# Sample List: [1, 5, 9, 6, 3, 1, 5, 3, 1, 9]
# count using count(): {1: 3, 3: 2, 5: 2, 6: 1, 9: 2}
# count using for loop: {1: 3, 3: 2, 5: 2, 6: 1, 9: 2}
# count using Counter: {1: 3, 3: 2, 5: 2, 6: 1, 9: 2}