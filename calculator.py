print("==== Simple Expression Calculator ====")
print("Examples: 3+7, 10-4, 6*2, 20/5")
print("Type 'exit' to close the calculator\n")

while True:
    expression = input("Enter expression: ")

    if expression.lower() == "exit":
        print("Calculator closed. Goodbye!")
        break

    try:
        result = eval(expression)
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except Exception:
        print("Invalid expression. Please try again.")
