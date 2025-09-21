# CORD-19 Dataset

## Required File

Download `metadata.csv` and place it in this folder.

## Download Instructions

1. Go to: https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge
2. Click "Download" (requires Kaggle account)
3. Extract the ZIP file
4. Copy `metadata.csv` to this `data/` folder

## Alternative: Kaggle API

```bash
pip install kaggle
kaggle datasets download -d allen-institute-for-ai/CORD-19-research-challenge
unzip CORD-19-research-challenge.zip
mv metadata.csv data/
```

## File Info

- **Size**: ~1.65GB
- **Records**: 1M+ COVID-19 research papers
- **Columns**: title, abstract, authors, publish_time, etc.

## Usage

```python
import pandas as pd
df = pd.read_csv('data/metadata.csv')
```

**Note**: File not included due to size. Download required.
