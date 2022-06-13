def count_elements(lst):
    l = set(lst)
    print("count element using count(): ")
    for ele in l:
        print(f"{ele}x{lst.count(ele)}")
    print()


if __name__ == "__main__":
    lst = [1, 5, 9, 6, 3, 1, 5, 3, 1, 9]
    print(f"Sample List: {lst}")
    count_elements(lst)


# Sample:

# Sample List: [1, 5, 9, 6, 3, 1, 5, 3, 1, 9]
# count element using count(): 
# 1x3
# 3x2
# 5x2
# 6x1
# 9x2