def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b, rounding = 2):
    return round(a / b, rounding)

is_over = False
while not is_over:    
    print("=" * 30)
    print(f"{'Calculator':^30}")
    print("=" * 30)
    print("\n")
    print("Menu")
    print("\n")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("\n")
    print("=" * 30)
    user_choice = int(input("Please choose (1-5) what you want to do?: "))
    if 1<= user_choice <=4:
        first_num = float(input("Please enter your first number: "))
        second_num = float(input("Please enter your second number: "))
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
            while second_num == 0:
                print("Error: Division by zero is mathematically undefined.")
                second_num = float(input("Please enter a non-zero second number: "))
            result = divide(a=first_num, b=second_num)
            print(f"Dividing {first_num} by {second_num} gives {result}")
    elif user_choice == 5:
        is_over = True
    else:
        print("Invalid Choice. Please select a number between 1 to 5.")