def cubeSum(n):
    result = 1
    for i in range(2, n+1):
        result = result + (i*i*i)
    
    return result


if __name__ == "__main__":
    n = int(input("Enter a number: ").strip())
    print(f"cubeSum of {n} is {cubeSum(n)}")


# Sample:

# Enter a number: 7
# cubeSum of 7 is 784

# Enter a number: 5
# cubeSum of 5 is 225