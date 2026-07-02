import pandas as pd

df = pd.read_json("pandas/data.json")

print(df)

df.to_json("pandas/output.json", orient="records", indent=2)

"""
* orient → Decides the structure of the JSON.
* indent → Decides how nicely the JSON is formatted (spacing).
"""