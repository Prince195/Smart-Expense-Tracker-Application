import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import os

class ExpenseTracker:

    def __init__(self):
        self.file_name = os.path.normpath(
            input("Enter CSV file path (example: C:/PythonProjects/expenses.csv): ")
        )

        self.categories = ["Food", "Transport", "Utilities", "Entertainment", "Other"]

        if not os.path.exists(self.file_name):
            pd.DataFrame(
                columns=["Date", "Amount", "Category", "Description"]
            ).to_csv(self.file_name, index=False)
            print("New CSV file created.")

        self.df = pd.read_csv(self.file_name)
        print("CSV file loaded successfully.")

    def add_expense(self, date, amount, category, description):

        if amount <= 0:
            print(" Amount must be positive")
            return

        if category not in self.categories:
            print("Invalid category")
            return

        new_data = {
            "Date": date,
            "Amount": amount,
            "Category": category,
            "Description": description
        }

        self.df = pd.concat([self.df, pd.DataFrame([new_data])], ignore_index=True)
        self.df.to_csv(self.file_name, index=False)
        print(" Expense added successfully")

    def get_summary(self):

        if self.df.empty:
            print("No data available")
            return

        amounts = np.array(self.df["Amount"])

        print("\n Expense Summary")
        print("Total Expense:", np.sum(amounts))
        print("Average Expense:", np.mean(amounts))

    def filter_expenses(self, category):

        filtered = self.df[self.df["Category"] == category]

        if filtered.empty:
            print("No records found")
        else:
            print(filtered)

    def generate_report(self):

        if self.df.empty:
            print("No data to generate report")
            return

        print("\n Expense Report")
        print(self.df.groupby("Category")["Amount"].sum())

    def visualize_data(self):

        if self.df.empty:
            print("No data to visualize")
            return

        plt.figure(figsize=(12, 8))

        # Bar Chart
        plt.subplot(2, 2, 1)
        self.df.groupby("Category")["Amount"].sum().plot(kind="bar")
        plt.title("Total Expense by Category")

        # Line Graph
        plt.subplot(2, 2, 2)
        self.df["Date"] = pd.to_datetime(self.df["Date"], format="%Y-%m-%d", errors="coerce")
        self.df.groupby("Date")["Amount"].sum().plot()
        plt.title("Expense Trend Over Time")

        # Pie Chart
        plt.subplot(2, 2, 3)
        self.df.groupby("Category")["Amount"].sum().plot(kind="pie", autopct="%1.1f%%")
        plt.ylabel("")
        plt.title("Expense Distribution")

        # Histogram
        plt.subplot(2, 2, 4)
        sns.histplot(self.df["Amount"], bins=10)
        plt.title("Expense Frequency")

        plt.tight_layout()
        plt.show()


# ========== MAIN PROGRAM ========== 

tracker = ExpenseTracker()

while True:
    print("\n===== Smart Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. Filter by Category")
    print("4. Generate Report")
    print("5. Visualize Data")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        date = input("Enter date (YYYY-MM-DD): ")
        amount = float(input("Enter amount: "))
        category = input("Enter category (Food/Transport/Utilities/Entertainment/Other): ")
        description = input("Enter description: ")
        tracker.add_expense(date, amount, category, description)
        
    elif choice == "2":
        tracker.get_summary()

    elif choice == "3":
        cat = input("Enter category: ")
        tracker.filter_expenses(cat)

    elif choice == "4":
        tracker.generate_report()

    elif choice == "5":
        tracker.visualize_data()

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice")




        # C:\Users\princ\OneDrive\Desktop\Python\python project\exam\expenses.csv