import pandas as pd

alter = pd.DataFrame({"x": [1, 2, 3, 4, 5]})

results = alter[alter["x"] > 3]

print(results)