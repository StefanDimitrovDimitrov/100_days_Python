# import pyautogue
#
# def clear():
#     pyautogui.hotkey('shift', 'c')

def calculator():


    def add(a, b):
        return a + b

    def subtraction(a, b):
        return a - b

    def multiplication(a, b):
        return a * b

    def division(a, b):
        if b == 0:
            return "You can't divide by 0"
        return a / b


    operations = {
        "+": add,
        "-": subtraction,
        "*": multiplication,
        "/": division,
    }


    def calculation(operation):
        if operation == "+":
            return add(a, b)
        elif operation == "-":
            return subtraction(a, b)
        elif operation == "*":
            return multiplication(a, b)
        elif operation == "/":
            return division(a, b)

    continue_calculation = True

    a = float(input("What is the first number? "))
    while continue_calculation:

        print("+")
        print("-")
        print("*")
        print("/")
        operation = input("Pick an operation: ")
        b = float(input("What's the next number?: "))
        answer = operations[operation](a, b)
        print(f"{a} {operation} {b} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") =="y":
            a = answer
        else:
            calculator()

calculator()