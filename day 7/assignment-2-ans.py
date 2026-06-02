# question: You have 2 csv files: sales_q1.csv and sales_q2.csv. The files have 3 columns each: product, units_sold, revenue. Merge them into a single csv. Add a custom column: quarter which will inform which csv the row is taken from. Summarize the total revenue per product across both quarters
from collections import defaultdict
import csv

q1 = [
    {'product': 'product a', 'units_sold': '120', 'revenue': '2400'},
    {'product': 'product b', 'units_sold': '80', 'revenue': '4250'},
    {'product': 'product c', 'units_sold': '100', 'revenue': '3560'}
]

q2 = [
    {'product': 'product a', 'units_sold': '170', 'revenue': '3570'},
    {'product': 'product b', 'units_sold': '150', 'revenue': '6590'}
]

def write_csv(filename, data):
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['product', 'units_sold', 'revenue'])
        writer.writeheader()
        writer.writerows(data)

write_csv('sales_q1.csv', q1)
write_csv('sales_q2.csv', q2)

# merge 2 csv files
combined = []
for filename, quarter in [('sales_q1.csv', 'Q1'), ('sales_q2.csv', 'Q2')]:
    with open(filename, 'r', encoding='utf-8', newline='') as f:
        for row in csv.DictReader(f):
            row["quarter"] = quarter
            combined.append(row)

# write the combined csv data
with open('sales_combined.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['product', 'units_sold', 'revenue', 'quarter'])
    writer.writeheader()
    writer.writerows(combined)

#revenue summary
totals = defaultdict(float)
for row in combined:
    totals[row['product']] += float(row['revenue'])

print("Revenue Summary")
for product, total in sorted(totals.items(), key=lambda x: -x[1]):
    print(f" {product:12}: Rs.{total:,.0f}")

