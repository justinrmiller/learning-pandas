import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

ages = titanic["Age"]

print(f"Ages:\n{ages.head()}")
print(f"Ages type:\n{type(ages)}")
print(f"Age/Sex type\n:{type(titanic[['Age', 'Sex']])}")
print(f"Age/Sex shape\n:{titanic[['Age', 'Sex']].shape}")

above_35 = titanic[titanic["Age"] > 35]

print(f"Above age 35:\n{above_35.head()}")
print(f"Above age 35 shape:\n{above_35.shape}")

class_23 = titanic[titanic["Pclass"].isin([2, 3])]

print(f"Class 2,3:\n{class_23.head()}")
print(f"Class 2,3 shape:\n{class_23.shape}")

rows_10_25_col_3_5 = titanic.iloc[9:25, 2:5]

print(f"Rows 10 to 25, columns 3 to 5:\n{rows_10_25_col_3_5}")