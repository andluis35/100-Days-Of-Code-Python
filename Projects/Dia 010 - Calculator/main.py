import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def do_operation(n1, operations_dictionary):
    for symbol in operations_dictionary:
        print("[ " + symbol + " ]")
    operation = input("Pick an operation: ")
    print("---------------------------------")

    n2 = float(input("What's the second number?: "))
    print("---------------------------------")

    answer = operations[operation](n1, n2)

    print(f"{n1} {operation} {n2} = {answer}")

    return answer


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

should_continue = True

while should_continue:
    print(art.logo)
    print("=====================================")
    print("Welcome to the Anderson's Calculator!")
    print("=====================================")

    first_number = float(input("\nWhat's the first number?: "))
    print("---------------------------------")

    result = do_operation(first_number, operations)

    print("---------------------------------")
    choice = int(input(f"Choose an option:\n[1] Continue calculating with {result}\n[2] Start a new calculation\n[3] Stop\nR: "))

    if choice == 1:
        print("---------------------------------")
        while choice == 1:
            result = do_operation(result, operations)
            print("---------------------------------")
            choice = int(input(f"Choose an option:\n[1] Continue calculating with {result}\n[2] Start a new calculation\n[3] Stop\nR: "))

    elif choice == 2:
        print("\n" * 100)
        continue

    elif choice == 3:
        should_continue = False
        print("\n" * 100)
        print("+=+=+=+=+=+=+=+=+=+=+")
        print("Closing calculator...")
        print("+=+=+=+=+=+=+=+=+=+=+")

    else:
        print("Choose a valid option.")
