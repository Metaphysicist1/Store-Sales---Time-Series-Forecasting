
import matplotlib.pyplot as plt

def plot_time_series(df, column, title=None):
    """
    Plots a single column from a DataFrame against a datetime index to visualize trends over time.
    Aim: Useful for analyzing temporal patterns in specific data series.
    Usage: Call with a DataFrame, specify the column to plot, and optionally provide a title.
    Parameters: df (DataFrame with datetime index), column (str: column name to plot), title (str, optional: plot title).
    """
    plt.figure(figsize=(12, 4))
    plt.plot(df.index, df[column])
    plt.title(title if title else f"Time Series of {column}")
    plt.xlabel("Date")
    plt.ylabel(column)
    plt.tight_layout()
    plt.show()

def plot_all_time_series(df, columns=None, max_plots=10):
    """
    Plots multiple columns from a DataFrame to visualize several time series at once.
    Aim: Helps in comparing trends across different data series within the same DataFrame.
    Usage: Useful for exploratory data analysis; specify columns to focus on particular data series.
    Parameters: df (DataFrame with datetime index), columns (list, optional: specific columns to plot), max_plots (int, default 10: maximum number of plots).
    """
    if columns is None:
        columns = df.select_dtypes(include=['number', 'bool']).columns
    for i, col in enumerate(columns):
        if i >= max_plots:
            print(f"Only plotting first {max_plots} columns.")
            break
        plot_time_series(df, col)

def plot_all_dfs(dfs, columns_dict=None, max_plots=10):
    """
    Plots columns from multiple DataFrames to compare time series across different datasets.
    Aim: Facilitates comparative analysis across multiple DataFrames, highlighting differences or similarities.
    Usage: Ideal for analyzing related datasets; use columns_dict to specify columns for each DataFrame.
    Parameters: dfs (dict of DataFrames), columns_dict (dict, optional: specifies columns for each DataFrame), max_plots (int, default 10: maximum number of plots per DataFrame).
    """
    for name, df in dfs.items():
        print(f"\n--- {name} ---")
        cols = columns_dict[name] if columns_dict and name in columns_dict else None
        plot_all_time_series(df, columns=cols, max_plots=max_plots)