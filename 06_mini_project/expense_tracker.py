expenses = []
is_exit = False
while not is_exit:
    print("=" * 30)
    print(f"{'CLI Expense Tracker':^30}")
    print("=" * 30)
    print("\n")
    print("MENU")
    print("1. Add Expenses")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Highest Expense")
    print("5. Exit")
    print("\n")
    print("=" * 30)
    user_choice = int(input("Please choose from the menu (1-5), what you like to do?: "))
    if user_choice == 1:
        expenses_details = {}
        expenses_details["description"] = input("Please enter the description of your expenses: ").lower()
        expenses_details["amount"] = float(input("Please enter the amount: "))
        while expenses_details["amount"] <= 0:
            print("Amount cannot be 0 or negative.")
            expenses_details["amount"] = float(input("Please enter the amount: "))
        expenses_details["category"] = input("Please enter the category: ").lower()
        expenses.append(expenses_details)
    elif user_choice == 2:
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("=" * 30)
            print(f'{"Expenses Details":^30}')
            print("=" * 30)            
            for expense in expenses:
                print(f'{expense["description"].capitalize()}  =  Rs. {expense["amount"]:.2f} {expense["category"].capitalize()}')
            print("=" * 30)
    elif user_choice == 3:
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("=" * 30)
            print(f'{"Total Expenses":^30}')
            print("=" * 30)
            total_expenses = 0
            for expense in expenses:
                print(f'{expense["description"].capitalize()}  =  Rs. {expense["amount"]:.2f} {expense["category"].capitalize()}')
                total_expenses += expense["amount"]
            print(f'Total expenses: Rs.{total_expenses:.2f}')
            print("=" * 30)

    elif user_choice == 4:
        if not expenses:
            print("No expenses recorded yet.")
        else:
            print("=" * 30)
            print(f'{"Highest Expenses":^30}')
            print("=" * 30)
            highest_purchase = expenses[0]
            for expense in expenses:
                if expense["amount"] > highest_purchase["amount"]:
                    highest_purchase = expense
            print(f"{highest_purchase['description'].capitalize()} = Rs.{highest_purchase['amount']:.2f} {highest_purchase['category'].capitalize()}")
            print("=" * 30)
    else:
        is_exit = True     



