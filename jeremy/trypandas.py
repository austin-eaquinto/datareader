import pandas as pd
import matplotlib as plt


# dataset = "dataset.csv"
dataset = "duration_ms.csv"
df = pd.read_csv(dataset)

# print("\nDataset Overview:")
# print(df.info())
columns = df.columns
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

# # NEW DATAFRAME # #


def write_basic_csv(column, ascend=False):
    columns_to_keep = ["track_name", "artists", column]
    new_df = df[columns_to_keep].sort_values(column)
    new_df.to_csv(f"created_csvs/basic_{column}", index=False)

def write_csv(column, ascend=False):
    new_df = df.sort_values(column, ascending=ascend)
    new_df.to_csv(f"created_csvs/{column}", index=False)

# write_csv("duration_ms")
write_basic_csv("duration_ms")









def filter_tracks(condition, column, value):
    if condition == "equals":
        return df[df[column] == value]
    elif condition == "greater":
        return df[df[column] > value]
    elif condition == "less":
        return df[df[column] < value]
    elif condition == "contains":
        return df[df[column].fillna("").str.contains(value, case=False)]

def choose_columns(columns):
    return df[columns]

# print(filter_tracks("contains", "artists", "Estas Tonne"))

def list_columns():
    i = 0
    for column in columns: # first 2 are not useful. change for other datasets - probably just print all columns.
        print(i + 1, column)
        i += 1
    return i

def select_column():
    count = list_columns()
    print(f"choose column (1 - {count})")
    selection = input("> ")
    return int(selection) - 1

def select_columns():
    count = list_columns()
    print(f"choose column (1 - {count})")
    print("type a number and press enter. type 0 when finished.")
    chosen_list = []
    selection = input("> ")
    while selection != "0":
        chosen_list.append(int(selection) - 1)
        selection = input("> ")
    return chosen_list

# selected = select_column()
# print(selected)
# print(columns[selected])


def unique_of_column(column):
    return df[column].unique()


# unique_columns = unique_of_column(columns[selected])
# for item in unique_columns:
    # print(item)

durationVartist = df[["artists", "duration_ms"]] 