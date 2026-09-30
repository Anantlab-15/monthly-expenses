# Student Pocket Money & Monthly Expense Tracker

## Project Title
Student Pocket Money & Monthly Expense Tracker

## Domain
Personal Finance / Daily Productivity

## 1. Problem Statement

Students living on a fixed monthly pocket money often struggle to keep track of their small, daily cash spends (such as canteen snacks, bus fare, stationery, and tea). Because these expenses are small and paid in cash, students easily lose count and run out of money before the month ends.

This project is a **simple, menu-driven terminal tool** that helps a student:

1. Set their monthly pocket money limit.
2. Record day-to-day expenses with date, category, amount, and note.
3. View all expenses in an organized table.
4. Calculate category-wise totals using a Python dictionary.
5. Check their remaining balance and see if they are overspending.

## 2. Python Concepts Used

* **Functions (`def`):** Modular code where each task has its own function (`set_budget()`, `add_expense()`, `view_all_expenses()`, `category_summary()`, `view_report()`).
* **Lists:** A main list `expenses = []` that stores all transaction records in memory.
* **Dictionaries:**
  * Used for each record: `{"date": date, "category": category, "amount": amount, "note": note}`.
  * Used for category aggregation: `category_totals[category] = amount`.
* **Loops:**
  * `while True` loop to keep the interactive menu running.
  * `for` loop to iterate over items in the list and dictionary.
* **Conditional Statements:** `if-elif-else` to process menu choices and check whether spending exceeds the budget.

## 3. Project Requirements

Before running the project, make sure the following are installed:

* **Python 3.x**
* A terminal or command prompt
* A text editor or Python IDE such as VS Code, IDLE, or PyCharm

The project is designed as a terminal-based Python program.

### Dependencies

The project uses standard Python concepts and does not require any external Python packages based on the project description.

Therefore, there are **no `pip install` dependencies** required.

## 4. Environment Setup

### Step 1: Install Python

Install Python 3.x on your computer if it is not already installed.

After installation, open a terminal or command prompt and check the installation:
python --version

On some systems, including Windows, you may need to use:
py --version

Make sure the command displays a Python 3.x version.

### Step 2: Get the Repository

Clone the repository using Git:
git clone <repository-url>

Then move into the project directory:
cd <repository-folder>

Alternatively, if the repository has already been downloaded as a ZIP file, extract it and open a terminal inside the project folder.

### Step 3: Verify the Project Files

Make sure the repository contains:

* `README.md` at the root level
* The Python source file containing the Student Pocket Money & Monthly Expense Tracker program

## 5. Configuration

This project does not require API keys, database credentials, environment variables, or other external configuration based on the current project description.

No `.env` file is required.

The monthly pocket money limit is entered by the user when the program is running.

## 6. How to Run the Project

### Step 1: Open the Project Directory

Open a terminal or command prompt in the repository's root directory.

### Step 2: Run the Python Program

Run the Python source file that contains the project:

python <python-file-name>.py


On Windows, if `python` is not recognized, use:


py <python-file-name>.py

Replace `<python-file-name>.py` with the actual Python file name present in the repository.

### Step 3: Use the Menu

After starting the program, follow the menu displayed in the terminal.

The program allows the user to:

1. Set the monthly pocket money limit.
2. Add an expense by entering its date, category, amount, and note.
3. View all recorded expenses.
4. View category-wise expense totals.
5. View the overall report, including the remaining balance and spending status.

## 7. How the Project Works

The project keeps expense records in a Python list while the program is running.

Each expense is represented using a dictionary containing:

```python
{
    "date": date,
    "category": category,
    "amount": amount,
    "note": note
}
```

Category-wise spending is calculated using another dictionary. The program compares total spending with the monthly pocket money limit to determine the remaining balance and whether spending has exceeded the budget.

## 8. Important Note About Data

The project description specifies that the main expense list stores records **in memory**.

Therefore, unless the project source code contains an additional file/database storage mechanism, expense records are not expected to persist automatically after the program is closed.

## 9. Example Usage Flow

A typical session can follow this sequence:

```text
Start Program
     ↓
Set Monthly Pocket Money
     ↓
Add Daily Expenses
     ↓
View All Expenses
     ↓
View Category Summary
     ↓
View Overall Report
     ↓
Check Remaining Balance
```

For example, a student can record expenses such as:

* Canteen snacks
* Bus fare
* Stationery
* Tea

The program then organizes these expenses and calculates the corresponding totals.

## 10. Troubleshooting

### Python is not recognized

If the terminal says that `python` is not recognized, verify that Python 3.x is installed and added to the system PATH.

On Windows, try:

py --version
and then:
py <python-file-name>.py

### The program does not start

Make sure that:

1. You are inside the project/repository directory.
2. You are using the correct Python source filename.
3. Python 3.x is installed correctly.
4. You are running the program with Python rather than opening the source file directly.

### No expenses are visible after restarting

The project description specifies that the main `expenses` list stores records in memory. If the source code does not implement file or database storage, previously entered expenses will not be available after the program is closed.

## 11. Project Structure

A typical repository structure is:

```text
project-root/
│
├── README.md
└── <python-file-name>.py
```

If additional files are present in the repository, they should be described here according to their actual purpose.

## 12. Project Features

* Monthly pocket money/budget setup
* Daily expense recording
* Expense categorization
* Organized expense display
* Category-wise expense calculation
* Remaining balance calculation
* Overspending check
* Menu-driven terminal interface

## 13. Conclusion

The Student Pocket Money & Monthly Expense Tracker provides a simple way for students to monitor daily spending against a monthly pocket money limit. It demonstrates fundamental Python programming concepts such as functions, lists, dictionaries, loops, and conditional statements while solving a practical daily budgeting problem.
