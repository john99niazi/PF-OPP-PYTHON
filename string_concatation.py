##############################
'''string1=str(input("enter the first string 1:::"))
string2=str(input("enter the first string 2:::"))

STRING_CON=(string1+" "+string2)
print(STRING_CON)'''



###############################
'''Concatenation with Conditional Statements:
Write a Python program that takes a string and a number from the user.
Concatenate the string with itself only if the number is even, 
otherwise concatenate the string with "odd". Display the result.'''
################################


STRING=str(input("entr the string:::"))
num=int(input("enter the number:::"))

if num%2==0:
    result=(STRING*2)
else:
    result=STRING+"ODD"

print("RESULT IS::::"," ",result)