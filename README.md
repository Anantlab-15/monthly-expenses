# Problem Statement & Project Synopsis

## Project Title
Student Pocket Money & Expense Tracker

## Domain
Personal Finance / Daily Productivity

## Level
Class 12th Computer Science / Python Fundamentals

## Language
Python 3 (Terminal Only, Pure Standard Features)

---

## 1. Problem Statement
Students living on a fixed monthly pocket money often struggle to keep track of their small, daily cash spends (such as canteen snacks, bus fare, stationery, and tea). Because these expenses are small and paid in cash, students easily lose count and run out of money before the month ends.

This project is a **simple, menu-driven terminal tool** that helps a student:
1. Set their monthly pocket money limit.
2. Record day-to-day expenses with date, category, amount, and note.
3. View all expenses in an organized table.
4. Calculate category-wise totals using a Python dictionary.
5. Check their remaining balance and see if they are overspending.

---

## 2. Python Concepts Used (Class 12 Syllabus)
* **Functions (`def`):** Modular code where each task has its own function (`set_budget()`, `add_expense()`, `view_all_expenses()`, `category_summary()`, `view_report()`).
* **Lists:** A main list `expenses = []` that stores all transaction records in memory.
* **Dictionaries:**
  * Used for each record: `{"date": date, "category": category, "amount": amount, "note": note}`.
  * Used for category aggregation: `category_totals[category] = amount`.
* **Loops:**
  * `while True` loop to keep the interactive menu running.
  * `for` loop to iterate over items in the list and dictionary.
* **Conditional Statements:** `if-elif-else` to process menu choices and check whether spending exceeds the budget.

---

## 3. How to Run the Project
Open your terminal or command prompt in this directory and run:

```bash
python expense_tracker.py
```
