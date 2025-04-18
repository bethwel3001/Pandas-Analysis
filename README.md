# Iris Dataset Analysis Project

## Overview

This project demonstrates a complete data analysis workflow on the classic Iris dataset. The analysis includes loading the dataset, exploring and cleaning the data, performing basic statistical analysis, and creating various visualizations to gain insights.

## Project Structure

- `data_loading.py`: Contains the function to load the Iris dataset from scikit-learn and convert it into a pandas DataFrame.
- `data_analysis.py`: Implements dataset exploration, cleaning, basic statistics, and grouping operations.
- `data_visualization.py`: Provides functions to create line charts, bar charts, histograms, and scatter plots using matplotlib and seaborn.
- `import.py`: The main script that orchestrates the workflow by calling functions from the other modules.

## Dataset

The Iris dataset is loaded using the `load_iris()` function from the `sklearn.datasets` module. This dataset is bundled with scikit-learn and does not require an internet connection to access.

## Analysis Tasks

1. **Load and Explore the Dataset**
   - Load the Iris dataset into a pandas DataFrame.
   - Display the first few rows to inspect the data.
   - Check data types and identify any missing values.
   - Clean the dataset by handling missing values if any.

2. **Basic Data Analysis**
   - Compute basic statistics such as mean, median, and standard deviation.
   - Perform grouping by the target class and compute mean values for numerical features.
   - Identify patterns and insights from the data.

3. **Data Visualization**
   - Create a line chart showing trends over the dataset index.
   - Create a bar chart comparing average petal length across species.
   - Create a histogram to understand the distribution of sepal width.
   - Create a scatter plot to visualize the relationship between sepal length and petal length, colored by species.

## Usage

Run the main script to execute the full analysis and visualization workflow:

```bash
python import.py
```

Ensure the required Python packages are installed:

```bash
pip install pandas matplotlib seaborn scikit-learn
```

## Error Handling

The code includes basic error handling to manage issues during data loading, cleaning, and plotting.

## Conclusion

This project provides a clean, modular, and professional example of data analysis using Python's scientific libraries. It can be extended to other datasets and analysis tasks as needed.
