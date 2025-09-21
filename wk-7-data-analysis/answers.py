import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# Load dataset
try:
    df = pd.read_csv("cereal.csv")
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: cereal.csv not found in the directory. Please check the path.")
    df = None  # define df as None so script doesn’t break

if df is not None:
    # Display first few rows and dataset info
    print("First 5 rows of the dataset:")
    print(df.head(), "\n")

    print("Dataset info:")
    print(df.info(), "\n")

    # Check missing values
    print("Missing values per column:")
    print(df.isnull().sum(), "\n")

    # Clean dataset (drop missing values)
    df.dropna(inplace=True)


    # Task 2: Basic Data Analysis

    # Summary statistics
    print("Summary statistics:")
    print(df.describe(), "\n")

    # Map manufacturer letters to full names
    mfr_map = {
        "G": "General Mills",
        "K": "Kellogg's",
        "N": "Nabisco",
        "P": "Post",
        "Q": "Quaker Oats",
        "R": "Ralston"
    }
    df["mfr_full"] = df["mfr"].map(mfr_map)

    # Average rating by manufacturer
    avg_rating_by_mfr = df.groupby("mfr_full")["rating"].mean().sort_values(ascending=False)
    print("Average rating by manufacturer:")
    print(avg_rating_by_mfr, "\n")

    # Average calories by cereal type
    avg_calories_by_type = df.groupby("type")["calories"].mean()
    print("Average calories by cereal type:")
    print(avg_calories_by_type, "\n")


    # Task 3: Data Visualizations

    # 1. Line Chart: Ratings sorted by calories
    plt.figure(figsize=(8,5))
    df_sorted = df.sort_values("calories")
    plt.plot(df_sorted["calories"], df_sorted["rating"], marker="o", linestyle="-", color="blue")
    plt.title("Cereal Ratings by Calories")
    plt.xlabel("Calories")
    plt.ylabel("Rating")
    plt.grid(True)
    plt.show()

    # 2. Bar Chart: Average rating per manufacturer
    plt.figure(figsize=(8,5))
    sns.barplot(x=avg_rating_by_mfr.index, y=avg_rating_by_mfr.values, palette="Set2")
    plt.title("Average Rating by Manufacturer")
    plt.xlabel("Manufacturer")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45)
    plt.show()

    # 3. Histogram: Distribution of calories
    plt.figure(figsize=(8,5))
    plt.hist(df["calories"], bins=10, color="skyblue", edgecolor="black")
    plt.title("Distribution of Calories")
    plt.xlabel("Calories")
    plt.ylabel("Frequency")
    plt.show()

    # 4. Scatter Plot: Sugar vs Rating
    plt.figure(figsize=(8,5))
    plt.scatter(df["sugars"], df["rating"], color="green")
    plt.title("Cereal Sugar Content vs Rating")
    plt.xlabel("Sugars")
    plt.ylabel("Rating")
    plt.grid(True)
    plt.show()
