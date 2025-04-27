def pal(s):
     return s==s[::-1]

input_string=str(input("ENTER THE STRING"))

if pal(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

