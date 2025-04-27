'''k = int(input("Enter the range: "))
print("Enter the numbers:")

for i in range(k):
    num = int(input(f"Number {i + 1}: "))
print(f"Index {i}, Number {num}")
'''
'''
sum=0
for i in range(10):
    sum+=i
print(sum)'''

'''
sum=0
num=int(input("enter the number"))
for i in range(num):
    enter=int(input(f"Number {i + 1}: "))
    sum+=enter
print(sum)'''

"""
def sum_of_digits(numbers):
    result = []
    for number in numbers:
        digit_sum = sum(int(digit) for digit in str(number))
        result.append(digit_sum)
    return result

# Example usage:
numbers = [123, 456, 789, 101]
print("Original list:", numbers)
print("Sum of digits:", sum_of_digits(numbers))
"""

'''number =5
for i in range(1,11):
    mul=(f"{number}*{i}={number*i}")
    print(mul)'''
numbers=[1,2,3,4,5,6,98,6]
largest=numbers[0]
for number in numbers:
    if number > largest:
        largest=number
print(largest)


