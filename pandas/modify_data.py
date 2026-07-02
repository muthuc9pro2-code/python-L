import pandas as pd

modifed = pd.read_csv("pandas/modify_csv.csv", header=None, names=["name", "age", "place"])

print(modifed)