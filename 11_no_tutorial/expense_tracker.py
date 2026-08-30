import json
import os

filename = "expenses.json"

# ==========================================
# 1. DATA LAYER (File handling, silent functions)
# ==========================================

def load_expenses():
    if not os.path.exists(filename):
        return []
    else:
        with open(filename, "r") as file:
            try:
                expenses = json.load(file)
                return expenses
            except json.JSONDecodeError:
                return []

def save_expenses(expenses):
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)  

# ==========================================
# 2. BUSINESS LOGIC & INPUT VALIDATION LAYER
# ==========================================

def get_safe_float(prompt):
    while True:
        try:
            float_input = float(input(prompt))

            if float_input > 0:
                return float_input

            print("Input Error! amount can't be 0 or negative.")
            
        except ValueError:
            print("Invalid Input! Please enter positive number for amount.")

def get_safe_string(prompt):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input:
            return user_input
        print("Error! Input can't be blank")
        

# ==========================================
# 3. INTERACTIVE APPLICATION LAYER
# ==========================================

def add_expenses():
    expenses = load_expenses()
    expense_details = {}    
    if not expenses:
        expense_details["ID"] = 1
    else:
        expense_details["ID"] = expenses[-1]["ID"] + 1
    expense_details["description"] = get_safe_string("Please enter the description of your expense: ")
    expense_details["amount"] = get_safe_float("Please enter the amount of your expense: ")
    expense_details["category"] = get_safe_string("Please enter the category of your expense: ")
    expenses.append(expense_details)
    save_expenses(expenses)

def display_output(heading):    
    print("=" * 45)
    print(f"{heading:^45}")
    print("=" * 45)
    print(f"- {'ID':<4} | {'Description':<18} | {'Amount':>12} | {'Category'}")
    print()
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
    return expenses

def view_expenses():
    expenses = display_output("View Expenses")    
    for expense in expenses:
        print(f"- {expense['ID']:<4} | {expense['description'].capitalize():<18} | Rs. {expense['amount']:>8.2f} | {expense['category'].capitalize()}")
    print("=" * 45)

def calculate_total():
    expenses = display_output("Total Expenses")
    total_expenses = 0
    for expense in expenses:
        print(f"- {expense['ID']:<4} | {expense['description'].capitalize():<18} | Rs. {expense['amount']:>8.2f} | {expense['category'].capitalize()}")
        total_expenses += expense["amount"]
    print("-" * 45)
    print(f"{'':>7} {'Total Expenses':<19} | Rs. {total_expenses:>8.2f}")
    print("=" * 45)

def delete_expense():    
    view_expenses()
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    try:
        delete_id = int(input("Please enter the ID of expense you want to delete from above table: "))
              
    except ValueError:
        print("Invalid Input! Please enter the valid ID from the expense list.")
        return

    new_expenses_list =[]
    item_found = False

    for expense in expenses:
        if expense["ID"] == delete_id:
            item_found = True
        else:
            new_expenses_list.append(expense)
            
    if item_found:
        save_expenses(new_expenses_list)
        print(f"Successfully deleted the expense item with ID {delete_id}")
    else:
        print("No such expenses found. Please try again.")

def highest_expense():    
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    view_expenses()
    print("-" * 45)
    print("Here is the item with highest expense.")

    highest_expense = expenses[0]
    for expense in expenses:
        if expense["amount"] > highest_expense["amount"]:
            highest_expense = expense  

    print(f"- {highest_expense['ID']:<4} | {highest_expense['description'].capitalize():<18} | Rs. {highest_expense['amount']:>8.2f} | {highest_expense['category'].capitalize()}")
    print("-" * 45)

# ==========================================
# 4. MAIN PROGRAM LOOP
# ==========================================

def main():
    while True:
        print("=" * 45)
        print(f"{'CLI Expense Tracker':^45}")
        print("=" * 45)
        print("\n")
        print("MENU")
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Highest Expense")
        print("5. Delete Expense")
        print("6. Exit")
        print("\n")
        print("=" * 45)
        try:
            user_choice = int(input("Please choose what you want to do from the above menu. Select 1 to 6: "))
            if user_choice <=0 or user_choice > 6:
                print("Invalid Choice! please choose from 1 - 6 from the menu.")
                continue
        except ValueError:
            print("Invalid Input! You must enter 1 to 6 number.")
            continue
        if user_choice == 6:
            break
        if user_choice == 1:
            add_expenses()
        elif user_choice == 2:
            view_expenses()
        elif user_choice == 3:
            calculate_total()
        elif user_choice == 4:
            highest_expense()
        elif user_choice == 5:
            delete_expense()

if __name__ == '__main__':
    main()