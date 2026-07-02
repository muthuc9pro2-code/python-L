import pandas as pd

df = pd.read_csv("pandas/data_processing.csv")

df["total"] = df["Price"] * df["Quantity"]

grouped = df.groupby("Product")["total"].sum().reset_index()

sort_df = grouped.sort_values(by="total", ascending=False)

print("Sales Summary")
print(sort_df)