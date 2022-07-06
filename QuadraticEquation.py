#Quadratic Equation Calculator
#Author: Spencer Bowles
#Last Date Modified: July 1, 2022
#This program is intended to take inputs from the user and substitute them into the quadratic equation in order to produce a correct calculation.

import cmath

#Prompts for user inputs, and converts all values to float
a = float(input("Enter the coefficient 'a':" ))
b = float(input("Enter the coefficient 'b':" ))
c = float(input("Enter the coefficient 'c':" ))

#Calculate discriminant
d = b ** 2 - 4 * a * c

#Quadratic equation calculations
quadraticOne = (-b + cmath.sqrt(d)) / (2 * a)
quadraticTwo = (-b - cmath.sqrt(d)) / (2 * a)

print("x = " + str(quadraticOne) + ", or x = " + str(quadraticTwo))
