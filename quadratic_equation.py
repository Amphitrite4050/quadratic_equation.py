import math

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Calculate discriminant
d = b**2 - 4*a*c

# Check if the discriminant is positive, negative or zero
if d > 0:
    # Two real roots
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    print("The roots are", x1, "and", x2)
elif d == 0:
    # One real root
    x = -b / (2*a)
    print("The root is", x)
else:
    # Two complex roots
    real_part = -b / (
