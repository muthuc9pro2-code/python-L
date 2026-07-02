import pandas as pd

customers = pd.DataFrame({
    "CustomerID": [1, 2, 3],
    "Name": ["alice", "muthu", "nari"]
})

orders = pd.DataFrame({
    "OrdersID": [101, 102, 103, 104],
    "CustomerID": [1, 2, 1, 3],
    "Product": ["shirt", "pant", "shoes", "hat"]
})

output = pd.merge(customers, orders, on="CustomerID", how="inner")

print(output)