import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

movies = pd.read_csv("../data/movie_dataset.csv")
FILENAME = "../data/movies_cleaned.csv"

# Heatmap for missing values
# ax = plt.axes()
# sns.heatmap(movies.isna().transpose(), cbar=False, ax=ax)
# plt.xlabel("Columns")
# plt.ylabel("Missing values")
# plt.show()


# 1,0 for true/false because of correlation matrix below
# movies["missing_overview"] = np.where(movies["overview"].isna(), 1, 0)
# movies["release_date"] = pd.to_datetime(movies["release_date"])
# movies["age_of_movie"] = 2025 - movies["release_date"].dt.year
# columns_of_interest = ["age_of_movie", "budget", "popularity", "missing_overview", "runtime", "revenue","vote_average"]

# Spearman correlation is used to measure the strength and 
# direction of a monotonic relationship between two variables that are non continous/non linear
# correlation_matrix = movies[columns_of_interest].corr(method = "spearman")
# sns.set_theme(style="white")
# plt.figure(figsize=(8, 6))
# heatmap = sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar_kws={"label": "Spearman correlation"})
# heatmap.set_title("Correlation heatmap")
# plt.show()


# remove records with null empty values
# movies_missing = movies[
#     ~(movies["overview"].isna())       &
#     ~(movies["budget"].isna())         &
#     ~(movies["release_date"].isna())   &
#     ~(movies["popularity"].isna())     &
#     ~(movies["runtime"].isna())        &
#     ~(movies["revenue"].isna())        &
#     ~(movies["vote_average"].isna())   &
#     ~(movies["genres"].isna())         &
#     ~(movies["original_title"].isna()) 
# ]

# YIKES 1168 unique genres...
# print(movies_missing["genres"].nunique())

# Check if there are overview summaries with less than 15 words
#words = movies_missing["words_in_overview"] = movies_missing["overview"].str.split().str.len()
#print(words)


# all unique ids
#print(movies_missing["id"].nunique())

# prep for use with LLM?
# movies_missing["tagged_overview"] = movies_missing[["id","overview"]].astype(str).agg(" ".join, axis=1)
# print(movies_missing["tagged_overview"])

# print(movies_missing.info())

# Remove unnecessary columns
# def dothis():
#     movies_missing.drop(["missing_overview", "age_of_movie"], axis=1).to_csv("movies_cleaned.csv", index=False)
# dothis()


def generate_bar_graph(filename):
    genres = "Fantasy Action Adventure"

    filename_df = pd.read_csv(filename)

    action_movies = filename_df[filename_df["genres"].str.contains(genres, case=False, na=False)]
    top_5_action = action_movies.sort_values("popularity", ascending=False).head(5)

    plt.figure(figsize=(10,6))
    plt.bar(top_5_action["original_title"], top_5_action["popularity"], color="darkred")
    plt.xlabel("Movie Titles", fontsize=12)
    plt.ylabel("Popularity Score", fontsize=12)
    plt.title("Top 5 Most Popular Action Movies", fontsize=14, pad=20)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.yticks(fontsize=10)
    plt.tight_layout()
    plt.show()

generate_bar_graph(FILENAME)