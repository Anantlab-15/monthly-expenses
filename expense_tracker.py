# Project Name : Student Pocket Money & Expense Tracker

budget = 0.0
expenses = []  # List to store all expense records

# 1. FUNCTION: To set or update monthly pocket money budget
def set_budget():
    global budget
    print("\n    SET MONTHLY POCKET MONEY    ")
    amount = float(input("Enter your monthly pocket money (Rs): "))
    if amount <= 0:
        print("Budget must be greater than 0!")
        return
    budget = amount
    print("Success: Monthly pocket money set to Rs " , budget)

# 2. FUNCTION: To add a new expenses record
def add_expense():
    print("\n    ADD NEW EXPENSE    ")

    date = input("Enter date (e.g. 28-09): ").strip()
    if date == "":
        date = "Today"

    print("\nSelect Category:") 
    print("1. Food / Canteen")
    print("2. Travel / Bus / Auto")
    print("3. Stationery / Xerox")
    print("4. Snacks / Tea")
    print("5. Others")
    category_choice = input("Enter category choice (1-5): ").strip()
    categories = {"1": "Food","2": "Travel","3": "Stationery","4": "Snacks","5": "Others"}
    if category_choice in categories:
        category = categories[category_choice]
    else:
        print("Invalid choice! Setting category to 'Others'.")
        category = "Others"

    amount = float(input("Enter amount spent (Rs): "))
    if amount <= 0:
        print("Amount must be greater than 0!")
        return
    
    note = input("Enter note (e.g. Canteen burger, bus ticket): ").strip()
    if note == "":
        note = "No remark"
    record = {"date": date,"category": category,"amount": amount,"note": note}
    expenses.append(record)
    print("\nSuccess: Added Rs " , amount , "for" , category)
   
    if budget > 0:  # Checking if budget is exceeded or not
        total_spent = get_total_spent()
        if total_spent > budget:
            extra = total_spent - budget
            print("[ALERT] Warning: You have exceeded your pocket money by Rs " , extra)

# 3. FUNCTION: To calculate the total money spent
def get_total_spent():
    total = 0.0
    for item in expenses:
        total = total + item["amount"]
    return total

# 4. FUNCTION: Use to view all expenses that are recorded
def view_all_expenses():
    print("\n    LIST OF ALL EXPENSES    ")
    if len(expenses) == 0:
        print("No expenses recorded yet. Use Option 2 to add one.")
        return
    
    print("S.No" + " " * 4 + "Date" + " " * 8 + "Category" + " " * 10 + "Amount (Rs)" + " " * 2 + "Note") #Heading
    sno = 1
    total = 0.0
    for item in expenses:
        print(sno , " " * 4 ,  item['date'] , " " * 8 , item['category'] , " " * 10 , item['amount'] , " " * 2 , item['note'])
        total = total + item["amount"]
        sno = sno + 1
    print("Total Records: " , len(expenses) , "| Total Spent: Rs " , total)

# 5. FUNCTION: Use to catagorize expenses
def category_summary():
    print("\n    CATEGORY-WISE SUMMARY    ")
    if len(expenses) == 0:
        print("No expenses recorded yet.")
        return
    category_totals = {} # To store total amount for each category
    for item in expenses:
        cat = item["category"]
        amt = item["amount"]
        if cat in category_totals:
            category_totals[cat] = category_totals[cat] + amt
        else:
            category_totals[cat] = amt
    print("Category" + " " * 15 + "Total Spent (Rs)")
    for cat in category_totals:
        print(cat + " " * 15 + str(category_totals[cat]))

# 6. FUNCTION: To see financial report and status of monthly budget
def view_report():
    print("\n    FINANCIAL REPORT    ")
    total_spent = get_total_spent()
    remaining = budget - total_spent

    print("1. Monthly Pocket Money : Rs " , budget)
    print("2. Total Money Spent    : Rs " , total_spent)

    if budget > 0:
        if remaining >= 0:
            print("3. Remaining Balance    : Rs " , remaining)
            print("   Status               : Safe (Within Budget)")
        else:
            print("3. Overspent Amount     : Rs " , abs(remaining))
            print("   Status               : Over Budget! Please control your spending.")
    else:
        print("3. Remaining Balance    : Budget not set yet (Use Option 1)")

    if len(expenses) > 0: # Use to identify highest spend category
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
        print("4. Highest Spending On  : " , max_cat  , " Rs " , max_amt )

# 7. MAIN FUNCTION
def main():
    while True:
        print(" ")
        print("   STUDENT POCKET MONEY & EXPENSE TRACKER   ")
        print("1. Set Monthly Pocket Money")
        print("2. Add New Expense")
        print("3. View All Expenses")
        print("4. View Category-wise Summary")
        print("5. View Financial Report")
        print("6. Exit")

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
main()