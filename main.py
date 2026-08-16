import csv
import os

FILE_NAME = "expenses.csv"


# Create file if it does not exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Type", "Amount", "Category", "Date", "Description"])


# Add a transaction
def add_transaction():
    transaction_type = input("Enter type (income/expense): ").lower()
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    date = input("Enter date (DD-MM-YYYY): ")
    description = input("Enter description: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            transaction_type,
            amount,
            category,
            date,
            description
        ])

    print("Transaction added successfully!")


# View all transactions
def view_transactions():
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        print("\n--- All Transactions ---")

        found = False

        for row in reader:
            found = True
            print(
                f"Type: {row['Type']} | "
                f"Amount: ₹{row['Amount']} | "
                f"Category: {row['Category']} | "
                f"Date: {row['Date']} | "
                f"Description: {row['Description']}"
            )

        if not found:
            print("No transactions found.")


# Calculate financial summary
def show_summary():
    total_income = 0
    total_expense = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Type"] == "income":
                total_income += float(row["Amount"])
            elif row["Type"] == "expense":
                total_expense += float(row["Amount"])

    balance = total_income - total_expense

    print("\n--- Financial Summary ---")
    print("Total Income  :", total_income)
    print("Total Expenses:", total_expense)
    print("Balance       :", balance)


# Delete a transaction
def delete_transaction():
    transactions = []

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        transactions = list(reader)

    if not transactions:
        print("No transactions available.")
        return

    print("\n--- Transactions ---")

    for i, row in enumerate(transactions, start=1):
        print(
            i,
            row["Type"],
            row["Amount"],
            row["Category"],
            row["Date"],
            row["Description"]
        )

    choice = int(input("Enter transaction number to delete: "))

    if 1 <= choice <= len(transactions):
        transactions.pop(choice - 1)

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "Type",
                    "Amount",
                    "Category",
                    "Date",
                    "Description"
                ]
            )

            writer.writeheader()
            writer.writerows(transactions)

        print("Transaction deleted successfully!")
    else:
        print("Invalid transaction number.")


# Main menu
def main():
    create_file()

    while True:
        print("\n==============================")
        print("     PERSONAL EXPENSE TRACKER")
        print("==============================")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Show Summary")
        print("4. Delete Transaction")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_transaction()

        elif choice == "2":
            view_transactions()

        elif choice == "3":
            show_summary()

        elif choice == "4":
            delete_transaction()

        elif choice == "5":
            print("Thank you for using Personal Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


main()