num1=int(input("give a number: "))
num2=int(input("give another number: "))
operator=input("give a operator + or - or * or / =")
if operator=="+":
    print(f"addition of two numbers is:{num1+num2}")
elif operator=="-":
    print(f"subtraction of two numbers is:{num1-num2}")
elif operator=="*":
    print(f"multiplication of two numbers is:{num1*num2}")
elif operator=="/":
    print(f"division of two numbers is:{num1/num2}")
else:
    print("invalid operator")