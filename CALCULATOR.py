def calculator():
    # Prompt user for input
    print("Welcome to the Simple Calculator!")
    
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        print("Choose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("Enter the operation (1/2/3/4): ")

        # Perform the chosen operation
        if choice == '1':
            result = num1 + num2
            operation = "+"
        elif choice == '2':
            result = num1 - num2
            operation = "-"
        elif choice == '3':
            result = num1 * num2
            operation = "*"
        elif choice == '4':
            if num2 == 0:
                return "Error: Division by zero is not allowed."
            result = num1 / num2
            operation = "/"
        else:
            return "Invalid operation choice."

        # Display the result
        return f"The result of {num1} {operation} {num2} is: {result}"

    except ValueError:
        return "Invalid input. Please enter numeric values."

# Call the calculator function
print(calculator())

