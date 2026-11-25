# Mini-Project: Expense Report Generator

import os
import csv
from datetime import date

# Verify that file exists before opening it
if not os.path.exists("../data/expenses.csv"):
        print("expenses.csv not found.")
else:
        # Read csv file into list of dictionaries 
        with open('../data/expenses.csv', 'r') as file:
                reader = csv.DictReader(file)
                rows = list(reader) 
        
        # Convert amount to float
        for row in rows: 
                row["amount"] = float(row["amount"])

        # Filter and total
        food_rows = [row for row in rows if row["category"] == "Food"]
        total = sum(row["amount"] for row in food_rows)
        
        # Today's date
        today = date.today().strftime("%B %d, %Y")

        # Write new report
        with open("food_report.txt", "w") as out:
                out.write(f"Food Expense Report - generated {today}\n")
                for row in food_rows:
                        out.write(f"{row['date']}: ${row['amount']:.2f}\n")
                out.write(f"Total: ${total:.2f}\n")
