def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b, rounding = 2):
    if b == 0:
        raise ZeroDivisionError("Error: Division by zero is mathematically undefined.")
    return round(a / b, rounding)

def get_safe_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
    

while True:
    is_user_choice_correct = False
    while not is_user_choice_correct: 
        print("=" * 40)
        print(f"{'Calculator':^40}")
        print("=" * 40)
        print("\n")
        print("Menu")
        print("\n")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        print("\n")
        print("=" * 40)

        try:              
            user_choice = int(input("Please choose (1-5) what you want to do?: "))

            if user_choice < 1 or user_choice > 5:
                print("Error: Please enter a number from 1 to 5.\n")
            else:
                is_user_choice_correct = True

        except ValueError:
            print("Error: Please enter valid numbers only.")
    # Exit condition
    if user_choice == 5:
        print("\nThank you for using Calculator! Goodbye.")
        break

    # Input Collection
    first_num = get_safe_float("Please enter your first number: ")
    second_num = get_safe_float("Please enter your second number: ")
    print("-" * 40)
    if user_choice == 1:
        result = add(a=first_num, b=second_num)
        print(f"Addition of {first_num} and {second_num} is {result:.2f}")
    elif user_choice == 2:
        result = subtract(a=first_num, b=second_num)
        print(f"Subtraction of {second_num} from {first_num} is {result:.2f}")
    elif user_choice == 3:
        result = multiply(a=first_num, b=second_num)
        print(f"Multiplication of {first_num} and {second_num} is {result:.2f}")
    elif user_choice == 4:
    
        try:
            result = divide(a=first_num, b=second_num)
            print(f"Dividing {first_num} by {second_num} gives {result:.2f}")
        except ZeroDivisionError as error:
            print(error)
            
    print("-" * 40 + "\n")