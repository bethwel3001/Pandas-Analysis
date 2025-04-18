from data_loading import load_iris_dataset
from data_analysis import explore_dataset, clean_dataset, basic_statistics, group_by_category
from data_visualization import plot_line_chart, plot_bar_chart, plot_histogram, plot_scatter

def main():
    # Load the Iris dataset
    df = load_iris_dataset()
    if df is None:
        print("Failed to load dataset. Exiting.")
        return

    # Task 1: Explore and clean the dataset
    explore_dataset(df)
    df_clean = clean_dataset(df)

    # Task 2: Basic data analysis
    basic_statistics(df_clean)
    # Group by 'target' and compute mean of 'sepal length (cm)'
    group_by_category(df_clean, 'target', 'sepal length (cm)')

    # Task 3: Data visualization
    # Line chart: Using index as x-axis and 'sepal length (cm)' as y-axis
    plot_line_chart(df_clean.reset_index(), 'index', 'sepal length (cm)')
    # Bar chart: average petal length per species (target)
    plot_bar_chart(df_clean, 'target', 'petal length (cm)')
    # Histogram: distribution of 'sepal width (cm)'
    plot_histogram(df_clean, 'sepal width (cm)')
    # Scatter plot: sepal length vs petal length, colored by target
    plot_scatter(df_clean, 'sepal length (cm)', 'petal length (cm)', 'target')

if __name__ == "__main__":
    main()
