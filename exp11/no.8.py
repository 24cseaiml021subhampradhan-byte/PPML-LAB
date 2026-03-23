import pandas as pd

df_csv = pd.read_csv("sample.csv")
print("Data frame from CSV:")
print(df_csv)

df_json = pd.read_json("sample.json")
print("\nDataFrame from JSON:\n", df_json)