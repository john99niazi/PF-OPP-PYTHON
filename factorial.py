num=int(input("enter the number"))

if num<0:
    print("it is not a factoriall")

if num==0:
    print("its factorial is 1")

fact=1
if num>0:
    for i in range(2,num+1):
        fact=fact*i
print(f" the factorial of {num} is {fact} ",)
