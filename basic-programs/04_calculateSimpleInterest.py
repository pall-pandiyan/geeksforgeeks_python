def calculateSimpleInterest(p, t, r):
    return (p*t*r/100)

if __name__=="__main__":
    p = float(input("Enter the Principle amount: ").strip())
    t = float(input("Enter the unit of Time: ").strip())
    r = float(input("Enter the Interest Rate for unit of Time: ").strip())
    

    print(f"Principle is {p}")
    print(f"unit of Time is {t}")
    print(f"Interest rate is {r}")
    si = calculateSimpleInterest(p, t, r)
    print(f"Simple Interest is {si}")



# sample

# Enter the Principle amount: 10000
# Enter the unit of Time: 5
# Enter the Interest Rate for unit of Time: 5
# Principle is 10000.0
# unit of Time is 5.0
# Interest rate is 5.0
# Simple Interest is 2500.0