def sumOfTwoNumbers(num1, num2):
    return (num1 + num2)

if __name__ == "__main__":
    num1 = int(input().strip())
    num2 = int(input().strip())
    print(f"Sum of {num1} and {num2} is {sumOfTwoNumbers(num1, num2)}")