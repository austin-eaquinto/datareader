import pandas as pd

dataset = "../movies_cleaned.csv"
df = pd.read_csv(dataset)

# columns = df.columns
# for c in columns:
#     print(c)


def filter_movies(condition, column, value):
    if condition == "equals":
        return df[df[column] == value]
    elif condition == "greater":
        return df[df[column] > value]
    elif condition == "less":
        return df[df[column] < value]
    elif condition == "contains":
        return df[df[column].fillna("").str.contains(value, case=False)]

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



def list_columns(df):
    i = 0
    columns = df.columns
    for column in columns:
        print(i + 1, column)
        i += 1
    return columns

def select_columns_limit(amount, df):
    columns = list_columns(df)
    count = 0
    print(f"choose column (1 - {len(columns)})")
    print("type a number and press enter.")
    chosen_list = []
    while count < amount:
        selection = input("> ")
        chosen_list.append(int(selection) - 1)
        count += 1
        if count == amount:
            continue
    
    return chosen_list



def custom_df(df, columns=2):
    chosen_columns = select_columns_limit(columns, df)
    new_df = df.iloc[:10, chosen_columns]
    return new_df.to_string(index=False)

print(custom_df(df))