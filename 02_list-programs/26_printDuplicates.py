from collections import Counter

def print_duplicates(lst):
    result = []
    l = set(lst)
    for ele in l:
        if lst.count(ele)>0:
            result.append(ele)
    print(f"duplicates using count(): {result}")

    d = dict(Counter(lst))
    # print(type(dict(d)))

    result = []
    for k in d:
        if d[k]>0:
            result.append(k)
    print(f"duplicates using Counter: {result}")



if __name__ == "__main__":
    lst = [1,1,20,10,30,3,10,5]
    print(f"Sample List: {lst}")
    print_duplicates(lst)


# Sample:

# Sample List: [1, 1, 20, 10, 30, 3, 10, 5]
# duplicates using count(): [1, 3, 5, 10, 20, 30]
# duplicates using Counter: [1, 20, 10, 30, 3, 5