def compound_interest(p, r, t):
    # total amount including principle
    amount = p * pow(1+r/100, t)
    
    # return only the compound interest
    ci = amount - p
    return ci

if __name__ == "__main__":
    p = float(input("Enter the Priciple amount: ").strip())
    r = float(input("Enter the rate of interest: ").strip())
    t = float(input("Enter the time units: ").strip())

    print(f"Principle: {p} Interest Rate: {r} Time: {t}")
    print(f"Compount Amount: {compound_interest(p, r, t)}")


# sample:

# Enter the Priciple amount: 1200
# Enter the rate of interest: 5.4
# Enter the time units: 2
# Principle: 1200.0 Interest Rate: 5.4 Time: 2.0
# Compount Amount: 133.0992000000001