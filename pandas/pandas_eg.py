import pandas as pd

data = {
    "Name": ["alice", "muthu", "gowtham"],
    "Age": [25, 22, 31],
    "city": ["Newyork", "london", "mumbai" ]
}

df = pd.DataFrame(data)
print(df.dtypes)
print(df)
print(df["Name"])