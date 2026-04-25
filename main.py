import json
import os

FILE = "expenses.json"

# Load existing data
def load_expenses():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save data
def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=4)

# Add expense
def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/etc): ")
    description = input("Enter description: ")

    expenses = load_expenses()
    expenses.append({
        "amount": amount,
        "category": category,
        "description": description
    })

    save_expenses(expenses)
    print("Expense added successfully!")

# View expenses
def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found")
        return

    for i, exp in enumerate(expenses, 1):
        print(f"{i}. ₹{exp['amount']} - {exp['category']} ({exp['description']})")

# Total expense
def total_expense():
    expenses = load_expenses()
    total = sum(exp["amount"] for exp in expenses)
    print(f"Total Expense: ₹{total}")

# Main menu
while True:
    print("\n==== Expense Tracker ====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice")