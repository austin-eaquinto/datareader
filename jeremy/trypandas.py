import pandas as pd
import matplotlib as plt

df = pd.read_csv("dataset.csv")

# print("\nDataset Overview:")
# print(df.info())
# columns = df.columns
# for c in columns:
#     print(c)

# genre_counts = df["track_genre"].value_counts()
# print("\nTracks per Genre:")
# print(genre_counts)

# print(df.head())

# def sort_by(column):
#     return df.sort_values(by=column, ascending=False)

# sorted_df = sort_by("popularity")
# sorted_df.to_csv("created_csvs/popularity", index=False)

def write_basic_csv(column, ascend=False):
    columns_to_keep = ["track_name", "artists", column]
    new_df = df[columns_to_keep].sort_values(column)
    new_df.to_csv(f"created_csvs/basic_{column}")

def write_csv(column, ascend=False):
    new_df = df.sort_values(column, ascending=ascend)
    new_df.to_csv(f"created_csvs/{column}")

# write_csv("duration_ms")
write_basic_csv("duration_ms")