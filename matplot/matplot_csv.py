import matplotlib.pyplot as mat
import csv

months = []
sales = []

with open("matplot/data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        months.append(row["month"])
        sales.append(int(row["sales"]))

mat.bar(months, sales, color="red")
mat.title("Monthly sales report")
mat.xlabel("month")
mat.ylabel("sales")
mat.grid(True)
mat.tight_layout()
mat.show()