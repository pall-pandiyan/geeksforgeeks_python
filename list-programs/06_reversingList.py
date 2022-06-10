if __name__ == "__main__":
    lst = [2,5,10,12,13,15,20,16,25,1,30]
    print(f"Sample List: {lst}")
    
    n = len(lst)
    for i in range((n+1)//2):
        adjI = n-1-i
        # temp = lst[i]
        # lst[i] = lst[adjI]
        # lst[adjI] = temp
        lst[i], lst[adjI] = lst[adjI], lst[i]
    print(f"Reverse using for loop: {lst}")

    lst = [2,5,10,12,13,15,20,16,25,1,30]
    start = 0
    end = n-1
    while(start<end):
        lst[start], lst[end] = lst[end], lst[start]
        start = start+1
        end = end-1
    print(f"Reverse using while loop: {lst}")