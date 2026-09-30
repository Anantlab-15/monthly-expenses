# ========================================================
# Project Name : Student Pocket Money & Expense Tracker
# ========================================================

# Global variables to store data in memory during program execution
budget = 0.0
expenses = []  # List of dictionaries to store all expense records


# ---------------------------------------------------------
# 1. FUNCTION: Set or update monthly pocket money
# ---------------------------------------------------------
def set_budget():
    global budget
    print("\n--- SET MONTHLY POCKET MONEY ---")
    amount = float(input("Enter your monthly pocket money (Rs): "))
    
    if amount <= 0:
        print("Budget must be greater than 0!")
        return

    budget = amount
    print(f"Success: Monthly pocket money set to Rs {budget:.2f}")


# ---------------------------------------------------------
# 2. FUNCTION: Add a new expense
# ---------------------------------------------------------
def add_expense():
    print("\n--- ADD NEW EXPENSE ---")

    # 1. Date
    date = input("Enter date (e.g. 28-09): ").strip()
    if date == "":
        date = "Today"

    # 2. Category selection using a dictionary
    print("\nSelect Category:")
    print("1. Food / Canteen")
    print("2. Travel / Bus / Auto")
    print("3. Stationery / Xerox")
    print("4. Snacks / Tea")
    print("5. Others")

    category_choice = input("Enter category choice (1-5): ").strip()
    
    categories = {
        "1": "Food",
        "2": "Travel",
        "3": "Stationery",
        "4": "Snacks",
        "5": "Others"
    }

    if category_choice in categories:
        category = categories[category_choice]
    else:
        print("Invalid choice! Setting category to 'Others'.")
        category = "Others"

    # 3. Amount
    amount = float(input("Enter amount spent (Rs): "))
    if amount <= 0:
        print("Amount must be greater than 0!")
        return

    # 4. Note / Description
    note = input("Enter note (e.g. Canteen burger, bus ticket): ").strip()
    if note == "":
        note = "No remark"

    # Create a dictionary for this expense record
    record = {
        "date": date,
        "category": category,
        "amount": amount,
        "note": note
    }

    # Add the dictionary to our main list
    expenses.append(record)
    print(f"\nSuccess: Added Rs {amount:.2f} for {category}!")

    # Check if budget is exceeded
    if budget > 0:
        total_spent = get_total_spent()
        if total_spent > budget:
            extra = total_spent - budget
            print(f"[ALERT] Warning: You have exceeded your pocket money by Rs {extra:.2f}!")


# ---------------------------------------------------------
# 3. FUNCTION: Calculate total spent so far
# ---------------------------------------------------------
def get_total_spent():
    total = 0.0
    for item in expenses:
        total = total + item["amount"]
    return total


# ---------------------------------------------------------
# 4. FUNCTION: View all recorded expenses
# ---------------------------------------------------------
def view_all_expenses():
    print("\n--- LIST OF ALL EXPENSES ---")
    if len(expenses) == 0:
        print("No expenses recorded yet. Use Option 2 to add one.")
        return

    # Table Header
    print("------------------------------------------------------------------")
    print(f"{'S.No':<5} {'Date':<12} {'Category':<15} {'Amount (Rs)':<12} {'Note'}")
    print("------------------------------------------------------------------")

    sno = 1
    total = 0.0
    for item in expenses:
        print(f"{sno:<5} {item['date']:<12} {item['category']:<15} {item['amount']:<12.2f} {item['note']}")
        total = total + item["amount"]
        sno = sno + 1

    print("------------------------------------------------------------------")
    print(f"Total Records: {len(expenses)} | Total Spent: Rs {total:.2f}")


# ---------------------------------------------------------
# 5. FUNCTION: Category-wise spending summary
# ---------------------------------------------------------
def category_summary():
    print("\n--- CATEGORY-WISE SUMMARY ---")
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return

    # Dictionary to store total amount for each category
    category_totals = {}

    for item in expenses:
        cat = item["category"]
        amt = item["amount"]

        if cat in category_totals:
            category_totals[cat] = category_totals[cat] + amt
        else:
            category_totals[cat] = amt

    # Display the summary
    print("---------------------------------------")
    print(f"{'Category':<20} {'Total Spent (Rs)':<15}")
    print("---------------------------------------")

    for cat in category_totals:
        print(f"{cat:<20} {category_totals[cat]:<15.2f}")

    print("---------------------------------------")


# ---------------------------------------------------------
# 6. FUNCTION: View financial report and status
# ---------------------------------------------------------
def view_report():
    print("\n================ FINANCIAL REPORT ================")
    total_spent = get_total_spent()
    remaining = budget - total_spent

    print(f"1. Monthly Pocket Money : Rs {budget:.2f}")
    print(f"2. Total Money Spent    : Rs {total_spent:.2f}")

    if budget > 0:
        if remaining >= 0:
            print(f"3. Remaining Balance    : Rs {remaining:.2f}")
            print("   Status               : Safe (Within Budget)")
        else:
            print(f"3. Overspent Amount     : Rs {abs(remaining):.2f}")
            print("   Status               : Over Budget! Please control your spending.")
    else:
        print("3. Remaining Balance    : Budget not set yet (Use Option 1)")

    # Find highest spend category
    if len(expenses) > 0:
        category_totals = {}
        for item in expenses:
            cat = item["category"]
            amt = item["amount"]
            if cat in category_totals:
                category_totals[cat] = category_totals[cat] + amt
            else:
                category_totals[cat] = amt

        max_cat = ""
        max_amt = 0.0
        for cat in category_totals:
            if category_totals[cat] > max_amt:
                max_amt = category_totals[cat]
                max_cat = cat

        print(f"4. Highest Spending On  : {max_cat} (Rs {max_amt:.2f})")

    print("==================================================")


# ---------------------------------------------------------
# 7. MAIN FUNCTION: Menu loop
# ---------------------------------------------------------
def main():
    while True:
        print("\n==========================================")
        print("   STUDENT POCKET MONEY & EXPENSE TRACKER")
        print("==========================================")
        print("1. Set Monthly Pocket Money")
        print("2. Add New Expense")
        print("3. View All Expenses")
        print("4. View Category-wise Summary")
        print("5. View Financial Report")
        print("6. Exit")
        print("==========================================")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            set_budget()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_all_expenses()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            view_report()
        elif choice == "6":
            print("\nThank you for using the tracker. Goodbye!\n")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


# Run the program
if __name__ == "__main__":
    main()
