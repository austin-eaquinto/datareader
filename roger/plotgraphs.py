import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/dataset.csv")

# # After loading the dataframe:
# print("First 5 rows:")
# print(df.head())  # Preview the data

# print("\nData summary:")
# print(df.info())  # Column names, data types, non-null counts

# print("\nDescriptive statistics:")
# print(df.describe())  # Numerical columns stats (mean, min, max, etc.)

# print("\nColumn names:")
# print(df.columns.tolist())  # List all columns

# track_dance = df[df.track_name > df.danceability]
# print("\ntrack_dance")
# print(track_dance)

# columns_to_keep = ["track_name", "artists"]
# new_df = df[columns_to_keep]
# print(new_df)

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

