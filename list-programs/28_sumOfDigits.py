def sumOfDigits(lst):
    print(f"sums using str():", end=" ")
    for num in lst:
        sum = 0
        for ch in str(num):
            sum += int(ch)
        print(sum, end=" ")
    print()

    print(f"sums using division:", end=" ")
    for num in lst:
        sum = 0
        while(num!=0):
            sum += num%10
            num = num//10
        print(sum, end=" ")
    print()

    # result = list(map(lambda ele: sum(int(sub) for sub in str(ele)), lst))
    # print(f"sums using map() and lambda: {result}")


if __name__ == "__main__":
    lst = [10,2,5,20,1,25,100,52,27]
    print(f"Sample List: {lst}")
    sumOfDigits(lst)


# Sample:

# Sample List: [10, 2, 5, 20, 1, 25, 100, 52, 27]
# sums using str(): 1 2 5 2 1 7 1 7 9
# sums using division: 1 2 5 2 1 7 1 7 9