import time
print("Welcome to my calculator")
time.sleep(1)
answer = input ("Do you want to add, substract, multiply or divide : ")
if answer == "add" or "Add" or "ADD":
        num1 = float(input ("First Number is : "))
        num2 = float(input ("Second Number is : "))
        num3 = num1 + num2
        print(num3)
elif answer == "substract" or "Substract" or "SUBSTRACT":
        print("You can substract here")
        num4 = float(input ("First Number is : "))
        num5 = float(input ("Second number is : "))
        num6 = num4 - num5
        print(num6)
elif answer == "multiply" or "Multiply" or "MULTIPLY":
        print("You can multiply here")
        num7 = float(input ("First Number is : "))
        num8 = float(input ("Second number is : "))
        num9 = num7 * num8
        print(num9)
elif answer == "divide" or "Divide" or "DIVIDE":
        print("You can divide here")
        num10 = float(input ("First Number is : "))
        num11 = float(input ("Second number is : "))
        num12 = num10 / num11
        print(num12)
else:
        print("Service not available")
print("Thank you for visiting")
