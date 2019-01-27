num1 = float(input("enter first number = "))
op = input("enter operation : ")
num2 = float(input("enter second number = "))

if op == "+":
    print("Addition = "+str(num1+num2))
elif op == "-":
    print("Difference = "+str(num1-num2))
elif op == "*":
    print("Multiplication = "+str(num1*num2))
elif op == "/":
    print("Division = "+str(num1/num2))
elif op == "%":
    print("Modulus = "+str(num1%num2))
else:
    print("operation not recognized")
