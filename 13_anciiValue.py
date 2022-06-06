def anciiValue(ch):
    return ord(ch)

if __name__ == "__main__":
    ch = input("Enter a charactor: ")
    if len(ch)>1:
        print(f"Error! Please enter only one charactor!")
    else:
        print(f"ANSII value of '{ch}' is {anciiValue(ch)}")


# Sample:

# Enter a charactor: g
# ANSII value of 'g' is 103

# Enter a charactor: c
# ANSII value of 'c' is 99

# Enter a charactor: 9
# ANSII value of '9' is 57