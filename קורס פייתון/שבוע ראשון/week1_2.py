num1=int(input("enter the number1"))
num2=int(input("enter the number2"))
num3=int(input("enter the number3"))
if(num1==num2+num3 or num2==num1+num3 or num3==num1+num2):
    print("the one number is the sum of two number")
else:
    print("the number is not sum of two number ")
