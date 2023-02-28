import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

print(f"Dataframe:\n{df}")
print(f"Describe (numerical data):\n{df.describe()}")
print(f"Age series:\n{df['Age']}")
