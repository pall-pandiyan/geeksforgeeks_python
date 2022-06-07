def cubeSum(n):
    temp = (n*(n+1)/2)
    return temp * temp


if __name__ == "__main__":
    n = float(input("Enter a number: ").strip())
    print(f"cubeSum of {n} is {cubeSum(n)}")


# Sample:

# Enter a number: 7.0
# cubeSum of 7.0 is 784.0

# Enter a number: 5.0
# cubeSum of 5.0 is 225