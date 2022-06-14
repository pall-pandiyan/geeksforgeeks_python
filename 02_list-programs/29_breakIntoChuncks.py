def breakChunks(lst, n):
    for i in range(0,len(lst),n):
        yield lst[i:i+n]

if __name__ == "__main__":
    lst = [1,12,135,4,88,79,132,54,61]
    n = 3
    print(f"Simple List: {lst}")
    print(f"n: {n}")
    result = list(breakChunks(lst, n))
    print("break using yield:", result)


# Sample:

# Simple List: [1, 12, 135, 4, 88, 79, 132, 54, 61]
# n: 3
# break using yield: [[1, 12, 135], [4, 88, 79], [132, 54, 61]]