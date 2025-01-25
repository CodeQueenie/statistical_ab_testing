import seaborn as sns
import matplotlib.pyplot as plt

def visualize_data(data, save_path="../results/plots"):
    """
    Create visualizations for conversion rates and distributions.

    Args:
        data (pd.DataFrame): Dataset containing 'group' and 'conversion' columns.
        save_path (str): Path to save the plots.

    Returns:
        None
    """
    import os
    os.makedirs(save_path, exist_ok=True)  # Ensure the directory exists

    # Bar plot for conversion rates
    conversion_rates = data.groupby("group")["conversion"].mean().reset_index()
    sns.barplot(x="group", y="conversion", data=conversion_rates, errorbar=None)
    plt.title("Conversion Rates by Group")
    plt.ylabel("Conversion Rate")
    plt.savefig(f"{save_path}/conversion_rates.png")
    plt.show()

    # Histogram of conversions
    sns.histplot(data, x="conversion", hue="group", multiple="dodge", shrink=0.8)
    plt.title("Histogram of Conversions by Group")
    plt.xlabel("Conversion")
    plt.savefig(f"{save_path}/conversion_histogram.png")
    plt.show()

# Example usage
if __name__ == "__main__":
    import pandas as pd
    from data_simulation import simulate_data

    # Simulate data and visualize
    data = simulate_data()
    visualize_data(data)