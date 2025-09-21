# Cereal Dataset Analysis 🥣

A comprehensive data analysis project that explores nutritional information and ratings of breakfast cereals using Python's data science stack.

## Overview

This project performs exploratory data analysis (EDA) on a cereal dataset, examining relationships between nutritional content, manufacturer, and consumer ratings through statistical analysis and visualizations.

## Features

✅ **Data Loading & Cleaning**: CSV import with error handling and missing value management  
✅ **Exploratory Analysis**: Summary statistics and manufacturer insights  
✅ **Data Visualization**: 4 different chart types showing key relationships  
✅ **Statistical Insights**: Grouped analysis by manufacturer and cereal type

## Requirements

```bash
pip install pandas matplotlib seaborn
```

**Libraries Used:**

- `pandas` - Data manipulation and analysis
- `matplotlib` - Basic plotting and visualization
- `seaborn` - Statistical data visualization

## Dataset Requirements

The script expects a `cereal.csv` file in the same directory with the following columns:

- `mfr` - Manufacturer code (G, K, N, P, Q, R)
- `rating` - Consumer rating score
- `calories` - Calories per serving
- `sugars` - Sugar content
- `type` - Cereal type (Hot/Cold)

## Installation & Usage

1. **Install dependencies:**

   ```bash
   pip install pandas matplotlib seaborn
   ```

2. **Place dataset:**

   - Ensure `cereal.csv` is in the same directory as the script
   - Download from: [Kaggle Cereal Dataset](https://www.kaggle.com/datasets/crawford/80-cereals)

3. **Run analysis:**
   ```bash
   python answers.py
   ```

## Sample Output

### Console Output

```
Dataset loaded successfully!

First 5 rows of the dataset:
        name mfr type  calories  protein  fat  sodium  fiber  carbo  sugars  potass  vitamins  shelf  weight  cups   rating
0  100% Bran   N    C        70        4    1     130     10   5.0       6     280        25      3     1.0  0.33  68.402973

Dataset info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 77 entries, 0 to 76
...

Average rating by manufacturer:
mfr_full
Nabisco          68.402973
General Mills    34.485852
Kellogg's        29.509541
...
```

## Key Insights Discovered

### Manufacturer Analysis

- **Best Rated**: Nabisco cereals typically have highest average ratings
- **Market Leaders**: General Mills and Kellogg's dominate volume but vary in quality
- **Niche Players**: Smaller manufacturers often focus on specific market segments

## File Structure

```
cereal-analysis/
├── answers.py        # Main analysis script
├── cereal.csv               # Dataset
├── README.md                # This documentation



## Statistical Methods Used

- **Descriptive Statistics**: Mean, median, standard deviation
- **Groupby Analysis**: Manufacturer and type-based aggregations
- **Correlation Analysis**: Visual correlation via scatter plots
- **Distribution Analysis**: Histogram frequency analysis


```
