'''Write a program that determines if a person is eligible for a bank loan based on the following criteria:

The person must be at least 21 years old.
The person must have a stable income of at least $30,000 per year.
If the person has a credit score of 700 or higher, the income requirement is reduced to $20,000 per year.
The person should not have any criminal record

person_name=str(input(" ENTER THE NAME OF PERSON  ::=" ))

person_age=int(input("ENTER THE AGE OF PERSON::::= "))

person_income=int(input("ENTER THE PERSON STABLE INCOME PER YEAR:::= "))

credit_score=int(input("ENTER THE CREADIT SCORE:::= "))

required_income=int(input("ENTER REQUIREMENT OF INCOME PER YEAR:::= "))

criminal_record=str(input("ENTER THE CRIMANAL RECORD  YES/NO :::=  "))

if person_age>=21 and person_income>=30000 and credit_score>=700 and required_income<=20000:
    print("**********"+person_name+"  "+"********** IS ELIGIBALE FOR LOAN******")
else:
    print("*********"+person_name+" "+" IS  NOT ELIGIBALE FOR LOAN******")
'''

##########################################################################################
'''
Write a program that calculates the final price of a product after applying multiple discounts based on the following criteria:

If the product price is greater than $500, apply a 10% discount.
If the customer is a member, apply an additional 5% discount.
If the customer has a coupon, apply an additional 10% discount.

'''

product_price=int(input(" ENTER THE PRICE OF PRODUCT:::"))
member=str(input(" ENTER THE MEMBER YES/NO :::"))
coupon=str(input("ENTER THE COUPON YES/NO :::"))
R1=0



if product_price>500:
    R1+=product_price*0.10
else:
    print(  "product price is low " , product_price  )
if member=="YES":
    R1+=product_price*0.5
else:
    print( "you have no coustemer membership")
if coupon=="YES":
    R1+=product_price*0.10
else:
    print("you have no coustmer  coupon::: ")

final_price = product_price - R1
print(" after all discounted your price is ", final_price)
