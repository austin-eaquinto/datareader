import pandas as pd

dataset = "../movies_cleaned.csv"
df = pd.read_csv(dataset)

columns = df.columns
for c in columns:
    print(c)


def list_columns():
    i = 0
    for column in columns:
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

def select_columns_limit(amount):
    column_count = list_columns()
    count = 0
    print(f"choose column (1 - {column_count})")
    print("type a number and press enter. type 0 when finished.")
    chosen_list = []
    while count <= amount:
        chosen_list.append(int(selection) - 1)
        count += 1

        if count == amount:
            continue
        selection = input("> ")
    
    return chosen_list






def custom_df(df):
    chosen_columns = select_columns_limit(2)
    new_df = df[chosen_columns]
    return new_df
