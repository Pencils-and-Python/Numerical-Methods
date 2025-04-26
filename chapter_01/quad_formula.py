"""
Summary:
--------
Program uses the quadratic fomula to calculate the roots of an expression.

Parameters:
-----------
ax^2 + bx = c

a = x^2 constant (a)
b = x costant (b)
c = constant (c)

Formula:
--------
x1 = (-b + (b^2 - 4ac)^(1/2))/2a
x2 = (-b - (b^2 - 4ac)^(1/2))/2a

>>> x^2−5x+6=0
x=2, x=3
>>> 2x^2−3x−2=0
x=−0.5,x=2

"""
import math 


print("Welcome to the Quadratic Root Calculator")
print("Please enter the constant for each element asked for in the formula format, ax^2 + bx = c/n")

# Input constants
a = float(input("Please enter the first constant, a: "))
b = float(input("Please enter the second constant, b: "))
c = float(input("Please enter the third constant, c: "))

# Calculations
def quad_roots(a, b, c):
    d = b**2 - 4*a*c
    if d >= 0:
        root_x1 = (-b+(math.sqrt(b**2-4*a*c)))/(2*a)
        root_x2 = (-b-(math.sqrt(b**2-4*a*c)))/(2*a)
        print(f'The roots to {a}x^2 + {b}x + {c} are as follows:')
        print(f'Root x1 = {root_x1}')
        print(f'Root x2 = {root_x2}')
        return root_x1, root_x2
    elif d == 0:
        root_x1 = -b/(2*a)
        print("The equation has a single root")
        return root_x1
    else:
        print("The equation has no real roots.")

quad_roots(a, b, c)




