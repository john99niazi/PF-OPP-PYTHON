'''Write a program that takes two numbers from the user and prints their sum.
num1=int(input("enter the first number  "))
num2=int(input("enter the second number  "))

add=num1+num2
print("sum of two numbers is ",add)'''

#######################################################################################################################

'''#Write a program to calculate the area of a circle. The radius should be provided by the user.
import math

r=float(input("enter the radius ::: "))
AREA_OF_CIRCLE=3.14*r*r     # ye bhee use kar skata ha
#AREA_OF_CIRCLE=math.pi*(r**2)# ye bhee use kar skata ha

print("AREA OF CIRCLE IS ",  AREA_OF_CIRCLE,   "WHOSE RADIUS IS THIS",  r)'''
##################################################################################################################################


'''Write a program that converts temperature from Celsius to Fahrenheit. The Celsius temperature should be provided by the user.

python
Cels=float(input("enter the celsius :::"))

frah=(9/5*Cels)+32

print("the farhenite is:::",frah)'''

######################################################################################################################
'''Write a program that solves a quadratic equation of the form ax^2 + bx + c = 0. The coefficients a, b, and c should be provided by the user.
import math
a=int(input("enter th cofficent a:::"))
b=int(input("enter th cofficent b:::"))
c=int(input("enter th cofficent c:::"))

disc=  b**2-4*a*c

if disc>0 :
    root1=(-b+math.sqrt(disc)/-2*a)
    root2=(-b-math.sqrt(disc)/-2*a)
    print("The roots are real and different.")
    print("Root 1:", root1)
    print("Root 2:", root2)
elif disc == 0:
    root = -b / (2*a)
    print("The roots are real and the same.")
    print("Root:", root)
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-disc) / (2*a)
    print("The roots are complex and different.")
    print("Root 1:", real_part, "+", imaginary_part, "i")
    print("Root 2:", real_part, "-", imaginary_part, "i")'''