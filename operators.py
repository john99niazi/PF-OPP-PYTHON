'''#Write a Python program #that takes two numbers from the user and performs addition, subtraction, multiplication, and division. Display the results for each operation.
num1=int(input("enter the number one :::"))
num2=int(input("enter the number 2:::"))

addition=num1+num2
subtr=num1-num2
mul=num1*num2
remin=num1%num2
quotient=num1/num2
rr=num1//num2
print("addition of two number is:::" , addition)               
print("subtraction of two number is:::", subtr)               
print("multiplication of two number is:::" ,mul)               
print("ramiander  of two number is:::",remin)               
print("quotient of two number is:::",quotient)               
print("rr of two number is:::", rr)               '''

##############################################################
#Comparison Operators:
#Write a Python program that takes two numbers from the user and compares them using all comparison operators (==, !=, >, <, >=, <=). Display the results of each comparison.
'''num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print(f"{num1}=={num2}:{num1==num2}")
print(f"{num1}>{num2}:{num1>num2}")
print(f"{num1}<{num2}:{num1<num2}")
print(f"{num1}=>{num2}:{num1>=num2}")
print(f"{num1}!={num2}:{num1!=num2}")'''

#Write a Python program that takes three boolean values from the user and applies logical and, or, and not operators. Display the results of each operation.
# Taking three boolean values as input from the user
bool1 = bool(int(input("Enter the first boolean value (0 or 1): ")))
bool2 = bool(int(input("Enter the second boolean value (0 or 1): ")))
bool3 = bool(int(input("Enter the third boolean value (0 or 1): ")))

# Performing logical operations
and_result = bool1 and bool2 and bool3
or_result = bool1 or bool2 or bool3
not_result = not bool1

# Displaying the results
print(f"{bool1} and {bool2} and {bool3}: {and_result}")
print(f"{bool1} or {bool2} or {bool3}: {or_result}")
print(f"not {bool1}: {not_result}")



###################################################################################################################
#Bitwise Operators:
#Write a Python program that takes two integers from the user and performs bitwise AND, OR, XOR, and NOT operations. Display the results of each operation
'''# Taking two integers as input from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Performing bitwise operations
bitwise_and = num1 & num2
bitwise_or = num1 | num2
bitwise_xor = num1 ^ num2
bitwise_not_num1 = ~num1
bitwise_not_num2 = ~num2

# Displaying the results
print(f"{num1} & {num2}: {bitwise_and}")
print(f"{num1} | {num2}: {bitwise_or}")
print(f"{num1} ^ {num2}: {bitwise_xor}")
print(f"~{num1}: {bitwise_not_num1}")
print(f"~{num2}: {bitwise_not_num2}")'''


