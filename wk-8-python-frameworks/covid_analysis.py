import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

sns.set(style="whitegrid")

# -------------------
# Step 1: Load Data
# -------------------

# Get the directory where this script resides
script_dir = os.path.dirname(os.path.abspath(__file__))

# Build the path to metadata.csv
file_path = os.path.join(script_dir, "data", "metadata.csv")

# Read the CSV
df = pd.read_csv(file_path)

print("Dataset shape:", df.shape)
print("\nData types and info:")
print(df.info())
print("\nFirst 5 rows:")
print(df.head())

# Check missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# -------------------
# Step 2: Data Cleaning
# -------------------
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df['abstract'] = df['abstract'].fillna('')
df['abstract_word_count'] = df['abstract'].apply(lambda x: len(x.split()))

# Drop rows missing essential info
df_clean = df.dropna(subset=['title', 'publish_time'])

# -------------------
# Step 3: Analysis & Visualizations
# -------------------

# 1. Publications per year
year_counts = df_clean['year'].value_counts().sort_index()
plt.figure(figsize=(8,5))
plt.bar(year_counts.index, year_counts.values, color='skyblue')
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.show()

# 2. Top journals
top_journals = df_clean['journal'].value_counts().head(10)
plt.figure(figsize=(10,5))
sns.barplot(x=top_journals.values, y=top_journals.index, palette="Set2")
plt.title("Top Journals Publishing COVID-19 Research")
plt.xlabel("Number of Papers")
plt.ylabel("Journal")
plt.show()

# 3. Word cloud of titles
titles_text = " ".join(df_clean['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles_text)
plt.figure(figsize=(15,7.5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# -------------------
# Step 4: Sample Data Output
# -------------------
print("\nSample cleaned data:")
print(df_clean[['title', 'year', 'journal', 'abstract_word_count']].sample(10))
