import matplotlib.pyplot as plt
import seaborn as sns

def plot_line_chart(df, x_col, y_col):
    """
    Plot a line chart showing trends over time or ordered data.
    Args:
        df (pd.DataFrame): The dataset.
        x_col (str): The column for x-axis.
        y_col (str): The column for y-axis.
    """
    try:
        plt.figure(figsize=(8, 5))
        plt.plot(df[x_col], df[y_col], marker='o')
        plt.title(f'Line Chart of {y_col} over {x_col}')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error plotting line chart: {e}")

def plot_bar_chart(df, category_col, numerical_col):
    """
    Plot a bar chart comparing numerical values across categories.
    Args:
        df (pd.DataFrame): The dataset.
        category_col (str): The categorical column.
        numerical_col (str): The numerical column.
    """
    try:
        plt.figure(figsize=(8, 5))
        sns.barplot(x=category_col, y=numerical_col, data=df)
        plt.title(f'Bar Chart of {numerical_col} by {category_col}')
        plt.xlabel(category_col)
        plt.ylabel(numerical_col)
        plt.show()
    except Exception as e:
        print(f"Error plotting bar chart: {e}")

def plot_histogram(df, numerical_col):
    """
    Plot a histogram to show the distribution of a numerical column.
    Args:
        df (pd.DataFrame): The dataset.
        numerical_col (str): The numerical column.
    """
    try:
        plt.figure(figsize=(8, 5))
        sns.histplot(df[numerical_col], kde=True)
        plt.title(f'Histogram of {numerical_col}')
        plt.xlabel(numerical_col)
        plt.ylabel('Frequency')
        plt.show()
    except Exception as e:
        print(f"Error plotting histogram: {e}")

def plot_scatter(df, x_col, y_col, hue_col=None):
    """
    Plot a scatter plot to visualize the relationship between two numerical columns.
    Args:
        df (pd.DataFrame): The dataset.
        x_col (str): The x-axis numerical column.
        y_col (str): The y-axis numerical column.
        hue_col (str, optional): The categorical column for color coding.
    """
    try:
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=x_col, y=y_col, hue=hue_col, data=df)
        plt.title(f'Scatter Plot of {y_col} vs {x_col}')
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        if hue_col:
            plt.legend(title=hue_col)
        plt.show()
    except Exception as e:
        print(f"Error plotting scatter plot: {e}")
