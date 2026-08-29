import json
import os

filename = "expenses.json"
def expenses_record():
    if os.path.exists(filename):
        with open(filename, "r") as file:
            try:                
                    expenses = json.load(file)            
            except json.JSONDecodeError:
                print("No expenses recorded yet.")
                expenses = []
    else:
        print("No expenses recorded yet.")
        expenses = []

    expenses_details = {}

    expenses_details["description"] = input("Please enter the description of your expenses: ").lower()
    expenses_details["amount"] = 0
    while expenses_details["amount"] <=0:
        try:
            temp_amount = float(input("Please enter the amount: "))
            if temp_amount <=0:
                print("Amount cannot be 0 or negative. Try again.")  
            else:
                expenses_details["amount"] = temp_amount

        except ValueError:
            print("Invalid Input! Please enter a positive number for amount.")

    expenses_details["category"] = input("Please enter the category: ").lower()
    expenses.append(expenses_details)

    with open(filename, "w") as file:        
        json.dump(expenses, file, indent=4)

    print(f"Success! Recorded expense for {expenses_details['description']}.")


is_exit = False

while not is_exit:
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
        user_choice = int(input("Please choose from the menu (1-6), what you like to do?: "))
        if user_choice < 1 or user_choice > 6:
            print("Invalid choice! Please choose from the menu 1 to 6.")
            continue
    except ValueError:
        print("Invalid choice! Please type a number between 1 and 6.")
        continue
    if user_choice == 1:
        expenses_record()
    elif user_choice == 2:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                expenses = json.load(file)

            print("\n" + "=" * 45)
            print(f'{"Expenses Details":^45}')
            print("=" * 30)            
            for expense in expenses:
                print(f'- {expense["description"].capitalize():<15}  =  Rs. {expense["amount"]:>7.2f} {expense["category"].capitalize()}')
            print("=" * 45)

        else:
            print("No expenses recorded yet.")

    elif user_choice == 3:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                expenses = json.load(file)

                print("\n" + "=" * 45)
                print(f'{"Total Expenses":^45}')
                print("=" * 45)
                
                total_expenses = 0
                for expense in expenses:
                    print(f'- {expense["description"].capitalize():<15}  =  Rs. {expense["amount"]:>7.2f} {expense["category"].capitalize()}')
                    total_expenses += expense["amount"]

                print("-" *45)
                print(f'Total expenses:   Rs.{total_expenses:>7.2f}')
                print("=" * 45)
                  
        else:
            print("No expenses recorded yet.")

    elif user_choice == 4:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                expenses = json.load(file)

                if not expenses:
                    print("No expenses recorded yet.")
                    continue

                print("=" * 45)
                print(f'{"Highest Expenses":^45}')
                print("=" * 45)

                highest_purchase = expenses[0]
                for expense in expenses:
                    if expense["amount"] > highest_purchase["amount"]:
                        highest_purchase = expense

                print(f"- {highest_purchase['description'].capitalize():<15} = Rs.{highest_purchase['amount']:>7.2f} {highest_purchase['category'].capitalize()}")
                print("=" * 45)

        else:
            print("No expenses recorded yet.")

    elif user_choice == 5:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                expenses = json.load(file)
                
            delete_expense = input("Please enter description of the item you want to delete: ").lower()

            updated_expenses = []
            item_found = False

            for expense in expenses:
                if expense["description"] == delete_expense:
                    item_found = True
                else:
                    updated_expenses.append(expense)

            if item_found:
                with open(filename, "w") as file:
                    json.dump(updated_expenses, file, indent=4)
                    print(f"Successfully deleted entry {delete_expense.capitalize()}.")
            else:
                print(f"No expense found matching {delete_expense.capitalize()}.")
        else:
            print("No expenses recorded yet.")

    else:
        is_exit = True