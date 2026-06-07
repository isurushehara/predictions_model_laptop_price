import pandas as pd

df = pd.read_csv("laptop.csv")

# Create Product column
df["Product"] = df["Company"] + " " + df["TypeName"]

# Move Product after Company
cols = list(df.columns)
cols.insert(2, cols.pop(cols.index("Product")))
df = df[cols]

df.to_csv("laptop_with_product.csv", index=False)

print(df.head())