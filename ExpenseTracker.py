expenses = []

def add_Expense():
    date = input("Enter a Date: ")
    item = input("Enter an Item: ")
    amt = float(input("Enter amount spent: ₹ "))
    expenses.append({"date": date, "item": item, "amt": amt})
    print("Expense added successfully!\n")

def show_tot():
    tot = sum(exp["amt"] for exp in expenses)
    print(f"Total expenses so far: ₹ {tot}\n")

def view_by_date():
    date = input("Enter date to view expenses (DD-MM-YYYY): ")
    found = False
    for exp in expenses:
        if exp["date"] == date:
            print(f"- {exp['item']}: {exp['amt']}")
            found = True

        if not found:
            print("No expenses found in this date\n")
        else:
            print()

def main():
    while True:
        print("=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. Show Total Expenses")
        print("3. View Expenses my Date")
        print("4. Exit")
        choice = input("Enter your Choice: ")

        if choice == '1':
            add_Expense()
        elif choice == '2':
            show_tot()
        elif choice == '3':
            view_by_date()
        elif choice == '4':
            print("Thank you for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
