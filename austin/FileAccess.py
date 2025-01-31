import pandas as pd
import matplotlib as plt

df = pd.read_csv("dataset.csv")

columns = df.columns
for c in columns:
    print(c)

# options for the file
# user enters information for specific data