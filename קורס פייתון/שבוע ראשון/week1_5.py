def number_is_num(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("is not number, try again")


def operator_is_oprator(prompt):
    while True:

        if(prompt!='+' and prompt!='-' and prompt!='*'and prompt!='/'):
            prompt=input("the operator is Illegal, try again")

        else: return prompt


num1=number_is_num("enter the firs number")
num2=number_is_num("enter the second number")
prompt=input("enter the operator")
operator=operator_is_oprator(prompt)
sum=0
if operator=='+':
    sum=num1+num2
elif operator=='-':
    sum=num1-num2
elif operator=='*':
    sum0=num1*num2
elif operator=='/':
    while (num2==0):
        num2=number_is_num("enter the second number")
        sum=num1/num2
print(sum)


