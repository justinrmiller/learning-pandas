import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

print(f"Titanic Head(8):\n{titanic.head(8)}")
print(f"Titanic dtypes:\n{titanic.dtypes}")

print("Writing titanic data to an Excel file (output_data/titanic.xlsx).")
titanic.to_excel("output_data/titanic.xlsx", sheet_name="passengers", index=False)

