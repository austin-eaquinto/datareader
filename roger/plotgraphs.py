import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/dataset.csv")

# # After loading the dataframe:
# print("First 5 rows:")
# print(df.head())  # Preview the data

# print("\nData summary:")
# print(df.info())  # Column names, data types, non-null counts

# print("\nDescriptive statistics:")
# print(df.describe())  # Numerical columns stats (mean, min, max, etc.)

# print("\nColumn names:")
# print(df.columns.tolist())  # List all columns

# Histogram of a feature
# plt.figure(figsize=(10,6))
# plt.hist(df['duration_ms']/60000, bins=20)  # Convert ms to minutes
# plt.title("Track Duration Distribution")
# plt.xlabel("Minutes")
# plt.ylabel("Number of Tracks")
# plt.show()


# # Scatter plot (e.g., loudness vs. energy)
# plt.scatter(df['loudness'], df['energy'], alpha=0.5)
# plt.title("Loudness vs Energy")
# plt.xlabel("Loudness (dB)")
# plt.ylabel("Energy")
# plt.show()

# Bar chart (top genres)
# genre_counts = df['track_genre'].value_counts().head(10)
# ax = genre_counts.plot(kind='bar', figsize=(10,6))  # Larger figure size
# plt.title("Top 10 Genres")
# plt.xticks(rotation=45)
# # Set y-axis limits (adjust these numbers based on your data)
# plt.ylim(0, genre_counts.max() + 50)  # Adds 50 units padding above highest bar
# # OR use a fixed value:
# # plt.ylim(0, 1500)  # Example: Force 0-1500 range
# plt.show()

# Bad Bunny, Bruno Mars, and Paramore have multiple genres
target_artist = "Drake"

# artist_df = df[df["artists"] == target_artist]

# Handle potential multi-artist entries
df_exploded = df.assign(artists=df["artists"].str.split(';')).explode("artists")

# Filter for the artist
artist_df = df_exploded[df_exploded['artists'] == target_artist]
print(artist_df["track_name"].unique())


# Get results
if not artist_df.empty:
    unique_genres = artist_df['track_genre'].unique()
    genre_counts = artist_df['track_genre'].value_counts()
    
    print(f"Artist: {target_artist}")
    print(f"Unique Genres: {len(unique_genres)}")
    print(genre_counts)
else:
    print(f"Artist '{target_artist}' not found in dataset.")


plt.title(target_artist)

# make a plot for x axis genres and y axis count for an artists bar chart