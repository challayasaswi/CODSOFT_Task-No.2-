def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        operation = input("Enter your choice ( 1 / 2 / 3 / 4 ): ")
        if operation in ["1", "2", "3", "4"]:
            break
        else:
            print("Invalid input. Please try again.")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == "1":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == "2":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == "3":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == "4":
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")

    play_again = input("Do you want to use the calculator again? (yes/no): ")
    if play_again.lower() == "yes":
        calculator()
    else:
        print("Thank you for visiting!")

calculator()