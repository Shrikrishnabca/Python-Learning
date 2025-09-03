# def calculator(first_number, second_number, operation):
#     if operation == "+":
#         result = first_number + second_number
#         print(f"{first_number} + {second_number} = {result}")
#         return result
#     elif operation == "-":
#         result = first_number - second_number
#         print(f"{first_number} - {second_number} = {result}")
#         return result
#     elif operation == "*":
#         result = first_number * second_number
#         print(f"{first_number} * {second_number} = {result}")
#         return result
#     elif operation == "/":
#         result = first_number / second_number
#         print(f"{first_number} / {second_number} = {result}")
#         return result
#     else:
#         return "Invalid operation"
#
#
# while True:
#     first_number = int(input("What's the first number?:"))
#     print("+\n-\n*\n/\n")
#     operation = input("Pick any operation:")
#     second_number = int(input("What's the next number"))
#     result = calculator(first_number, second_number, operation)
#     print(result)
#     is_continue = input(f"Type 'y' to continue calculating with {result} or type 'n' to start new calculation:")
#     if is_continue == 'y':
#         print("+\n-\n*\n/\n")
#         operation = input("Pick any operation:")
#         second_number = int(input("What's the next number"))
#         result = calculator(result, second_number, operation)
#         is_continue = input(f"Type 'y' to continue calculating with {result} or type 'n' to start new calculation:")
#     elif is_continue == "n":
#         print("\n" * 20)
#         first_number = int(input("What's the first number?:"))
#         print("+\n-\n*\n/\n")
#         operation = input("Pick any operation:")
#         second_number = int(input("What's the second number"))
#         result = calculator(first_number, second_number, operation)
#         is_continue = input(f"Type 'y' to continue calculating with {result} or type 'n' to start new calculation:")
#     else:
#         break

#TODO- create function for arithmetic operations
def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2

#TODO: store the operations
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}

# TODO: Take input use the dictionary
exit_all = False
while not exit_all:
    should_accumulate = True
    n1 = float(input("What's the first number?:"))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation = input("Pick any operation:")
        n2 = float(input("What's the next number?:"))
        result = operations[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result} or type 'n' to start new calculation or 'q' to stop calculation:")
        if choice == 'y':
            n1 = result
        elif choice == 'n':
            print("\n" * 20)
            should_accumulate = False
        else:
            should_accumulate = False
            exit_all = True

