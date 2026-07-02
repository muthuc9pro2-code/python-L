import pandas as pd

df = pd.read_csv("pandas/data.csv")

print(df)

df["Age"].to_csv("pandas/output.csv", index=False)


