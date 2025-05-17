# main.py
from ExpenseManager import ExpenseManager

def main():
    # Create an ExpenseManager object
    manager = ExpenseManager()

    while True:
        # Display a simple menu to the user
        print("\nExpense Manager")
        print("1. Add an expense")
        print("2. Delete an expense")
        print("3. List all expenses")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            manager.add_expense()
        elif choice == '2':
            manager.delete_expense()
        elif choice == '3':
            print("\nList of all expenses:")
            for expense in manager.list_expenses:
                print(expense)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
