from dataclasses import dataclass
import json
import os
from datetime import datetime

# =====================================================================
# 1. DATA MODEL (Class)
# =====================================================================
@dataclass
class Expense:
    id: int
    description: str
    amount: float
    category: str
    date: str

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
            "date": self.date
            }
# =====================================================================
# 2. CORE BUSINESS/DATABASE LAYER (Class)
# =====================================================================
class ExpenseTracker:
    def __init__(self, filepath: str = "expeses_oop.json"):
        self.filepath: str = filepath
        self.expenses: list[Expense] = []
        self.load_expenses()

    def save_expenses(self) -> None:
        dict_list = [expense.to_dict() for expense in self.expenses]

        with open(self.filepath, "w") as file:
            json.dump(dict_list, file, indent=4)

    def load_expenses(self) -> None:
        if not os.path.exists(self.filepath):
            self.expenses = []
            return
        try:
            with open(self.filepath, "r") as file:
                raw_data = json.load(file)
                if not isinstance(raw_data, list):
                    self.expenses = []
                    return
                for item in raw_data:
                    try:
                        required_keys = {"id", "description", "amount", "category", "date"}
                        if not required_keys.issubset(item.keys()):
                            raise KeyError(f"Missing keys in item: {item}")
                        expense_object = Expense(
                            id=int(item["id"]),
                            description=str(item["description"]),
                            amount=float(item["amount"]),
                            category=str(item["category"]),
                            date=str(item["date"])
                            )
                        self.expenses.append(expense_object)
                    except (ValueError, KeyError, TypeError) as item_error:
                        print(f"Skipping corrupted record inside JSON database: {item_error}")
                                
        except json.JSONDecodeError:
            print(f"Warning: '{self.filepath}' is corrupted or empty. Initializing a fresh list.")
            self.expenses = []
        except Exception as e:
            print(f"An unexpected error occured while loading data: {e}")
            self.expenses = []

       
    def add_expense(self, description: str, amount: float, category: str) -> bool:
        next_id = self.expenses[-1].id + 1 if self.expenses else 1
        current_date = datetime.now().strftime("%Y-%m-%d")

        new_expense = Expense(
            id=next_id,
            description=description,
            amount=amount,
            category=category,
            date=current_date
        )

        self.expenses.append(new_expense)
        self.save_expenses()
        return True

    def view_expenses(self) -> None:
        if not self.expenses:
            print("\nEmpty Tracker: No expenses recorded yet.")
            return

        print(f"{'ID':<4} | {'Description':<20} | {'Amount':<19} | {'Category':<8} | {'Date'}")
        print("-" * 75)

        for item in self.expenses:
            print(f"{item.id:<4} | {item.description:<20} | Rs. {item.amount:>15.2f} | {item.category:>8} | {item.date}")

        print("=" * 75)

    def delete_expense(self, expense_id: int) -> bool:
        if not self.expenses:
            print("\nEmpty Tracker: No expenses recorded yet.")
            return False

        updated_expenses = []
        item_found = False

        for item in self.expenses:
            if item.id == expense_id:
                item_found = True
            else:
                updated_expenses.append(item)

        if item_found:
            self.expenses = updated_expenses
            self.save_expenses()
            print(f"Successfully deleted the expense item with id {expense_id}.")
            return True
        else:
            print(f"No item found with ID {expense_id}.")
            return False

    def get_total(self) -> float:
        if not self.expenses:
            return 0.0

        return sum(item.amount for item in self.expenses)

    def get_highest(self) -> Expense | None:
        if not self.expenses:
            return None

        highest_expense = self.expenses[0]

        for item in self.expenses:
            if item.amount > highest_expense.amount:
                highest_expense = item

        return highest_expense
# =====================================================================
# 3. STANDALONE UI/INPUT UTILITIES (Normal Functions)
# =====================================================================
def get_safe_float(prompt: str) -> float:
    while True:
        try:
            float_input = float(input(prompt).strip())
            if float_input > 0:
                return float_input

            print("Input Error! amount must be greater than 0.")

        except ValueError:
            print("Invalid Input!: Please enter a valid number.")

def get_safe_string(prompt: str) -> str:
    while True:
        string_input = input(prompt).strip()
        if string_input:
            return string_input
        print("Invalid Input! input cannot be blank.")
# =====================================================================
# 3.1 Display Function (Normal Functions)
# =====================================================================
def header_display(heading):
    print('=' * 45)
    print(f"{heading:^45}")
    print("=" * 45)
# =====================================================================
# 4. RUNTIME / USER INTERFACE LAYER (Main Loop)
# =====================================================================
if __name__=='__main__':
    tracker = ExpenseTracker("expenses_oop.json")

    while True:
        header_display("EXPENSE TRACKER CLI (OOP)")
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
            user_choice = int(input("Please choose what you want to do from the above menu 1 to 6: ").strip())
            if user_choice <= 0 or user_choice > 6:
                print("Invalid Option: Please choose from menu 1 to 6.")
                continue
        except ValueError:
            print("Invalid Input: Please Choose a valid number from 1 to 6.")
            continue
        
        if user_choice == 6:
            print("\nThank you for using Expense Tracker. Goodbye!")
            break

        elif user_choice == 1:
            header_display("ADD NEW EXPENSES")
            desc = get_safe_string("Please enter description of your expense: ")
            amount = get_safe_float("Please enter amount: ")
            category = get_safe_string("Please enter category: ")

            tracker.add_expense(desc, amount, category)
            print("Expense added successfully.")
        elif user_choice == 2:
            header_display("VIEW ALL EXPENSES")
            tracker.view_expenses()

        elif user_choice == 3:
            header_display("TOTAL SPENDING")
            tracker.view_expenses()
            total_expenses = tracker.get_total()
            print(f"{'Total Expenses':>27} | Rs {total_expenses:>16.2f} |")
            print("=" * 45)
        elif user_choice == 4:
            header_display("HIGHEST EXPENSE RECORD")
            highest_expense = tracker.get_highest()

            if highest_expense:
                print(f"{'ID':<4} | {'Description':<20} | {'Amount':<19} | {'Category':<8} | {'Date'}")
                print("-" * 75)
                print(f"{highest_expense.id:<4} | {highest_expense.description:<20} | Rs. {highest_expense.amount:>15.2f} | {highest_expense.category:>8} | {highest_expense.date}")
                print("=" * 75)
            else:
                print("Empty Tracker: No expenses recorded yet.")

        elif user_choice == 5:
            header_display("DELETE AN EXPENSE")
            if not tracker.expenses:
                print("Empty Tracker: No expenses recorded to delete.")
                continue

            tracker.view_expenses()   

            try:
                delete_id = int(input("Please Enter ID of the expense you want to delete from the table above: ").strip())
            except ValueError:
                print("Invalid Input: Please enter a valid numerical ID")
                continue

            tracker.delete_expense(delete_id)
            input("\nPress Enter to return to the main menu...")