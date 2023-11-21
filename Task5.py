n1 = int(input("Enter first number."))
n2 = int(input("Enter second number."))
op = input("Enter an Operator.")

if op == '+':
    print("Sum = ", n1 + n2)
elif op == '-':
    print("Substraction: ", n1 - n2)
elif op == '*':
    print("Multiplication: ", n1*n2)
elif op == '/':
    if n1 > n2:
        print("Divison: ", n1/n2)
    else:
        print("Division: ",n2/n1)
else:
    print("Invalid Operator.")