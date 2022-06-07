from math import pi

def areaOfCircle(r):
    return pi*r*r

if __name__ == "__main__":
    radious = float(input("Enter the radious: ").strip())
    print(f"Radious is {radious}")
    print(f"Area is {areaOfCircle(radious)}")


# sample:

# Enter the radious: 5
# Radious is5.0
# Area is 78.53981633974483