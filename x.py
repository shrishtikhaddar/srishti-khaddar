num1 = float(input("Pehla number: "))
operator = input("Operator (+, -, *, /): ")
num2 = float(input("Dusra number: "))

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("0 se divide nahi kar sakte!")
else:
    print("Invalid operator!")
