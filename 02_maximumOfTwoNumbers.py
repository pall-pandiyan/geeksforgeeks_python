def maximumOfTwoNumbers(num1, num2):
    return num1 if num1 >= num2 else num2

if __name__ == "__main__":
    num1 = int(input("Enter first Number: ").strip())
    num2 = int(input("Enter second Number: ").strip())
    print(f"Maximum of {num1} and {num2} is {maximumOfTwoNumbers(num1, num2)}")