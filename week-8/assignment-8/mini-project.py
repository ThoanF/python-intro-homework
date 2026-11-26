# Mini-Project - Defensive CSV Reader

import csv

rows_attempted = 0
clean_data = []
skipped_rows = []

try:
    file = open("../data/messy_data.csv")
except FileNotFoundError:
    print("Error: messy_data.csv was not found.")
    exit()

reader = csv.DictReader(file)

for row_number, row in enumerate(reader, start=1):
    rows_attempted += 1

    if None in row:
        skipped_rows.append(f"Row {row_number}: extra column detected - skipped")
        continue

    try:
        amount = float(row["amount"])
        clean_row = {
            "name": row["name"],
            "category": row["category"],
            "amount": amount,
        }
        clean_data.append(clean_row)
    except ValueError:
        skipped_rows.append(f"Row {row_number}: ValueError - could not convert '{row['amount']}' to float")
    except KeyError:
        skipped_rows.append(f"Row {row_number}: KeyError - missing column")

file.close()

print("=== CSV Report ===")
print("Rows attempted:", rows_attempted)
print("Rows parsed:   ", len(clean_data))
print("Rows skipped:  ", len(skipped_rows))

print()
print("Skipped rows:")
for message in skipped_rows:
    print(" " + message)

print()
print("Clean data:")
for item in clean_data:
    print(f" {item['name']} | {item['category']} | ${item['amount']:.2f}")
