print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

option = int(input("Enter choice (1/2/3/4): "))

if option in [1, 2, 3, 4]:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if option == 1:
        result = num1 + num2
    elif option == 2:
        result = num1 - num2
    elif option == 3:
        result = num1 * num2
    elif option == 4:
        # Change to integer division if you want int result: result = num1 // num2
        result = num1 / num2

    print("The result of the operation is: {}".format(result))
else:
    print("Invalid operation entered")
    result = 0
    print("The result of the operation is: {}".format(result))
