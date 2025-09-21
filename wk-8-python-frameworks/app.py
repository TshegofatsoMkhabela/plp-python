# cord19_app.py
import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

sns.set(style="whitegrid")

# -------------------
# Step 1: Load Data
# -------------------
@st.cache_data
def load_data():
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "data", "metadata.csv")
    
    if not os.path.exists(file_path):
        st.error(f"CSV file not found at: {file_path}")
        return pd.DataFrame()  # Return empty DataFrame
    
    df = pd.read_csv(file_path)
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['abstract'] = df['abstract'].fillna('')
    df = df.dropna(subset=['title', 'publish_time'])
    return df

df = load_data()
if df.empty:
    st.stop()  # Stop execution if data cannot be loaded

# -------------------
# Step 2: App Layout
# -------------------
st.title("CORD-19 Data Explorer")
st.write("Interactive exploration of COVID-19 research papers.")

# Sidebar filters
year_min = int(df['year'].min())
year_max = int(df['year'].max())
year_range = st.sidebar.slider("Select year range", year_min, year_max, (year_min, year_max))

df_filtered = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# -------------------
# Step 3: Visualizations
# -------------------

# Publications by Year
st.subheader("Publications by Year")
year_counts = df_filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values, color='skyblue')
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# Top Journals
st.subheader("Top Journals")
top_journals = df_filtered['journal'].value_counts().head(10)
fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x=top_journals.values, y=top_journals.index, palette="Set2", ax=ax)
ax.set_xlabel("Number of Papers")
ax.set_ylabel("Journal")
st.pyplot(fig)

# Word Cloud of Titles
st.subheader("Word Cloud of Paper Titles")
titles_text = " ".join(df_filtered['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles_text)
fig, ax = plt.subplots(figsize=(15,7.5))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

# -------------------
# Step 4: Sample Data
# -------------------
st.subheader("Sample Data")
st.dataframe(df_filtered[['title', 'year', 'journal']].sample(min(10, len(df_filtered))))
