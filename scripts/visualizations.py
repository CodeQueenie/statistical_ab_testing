import seaborn as sns
import matplotlib.pyplot as plt

def visualize_data(data):
    """
    Create visualizations for conversion rates and distributions.

    Args:
        data (pd.DataFrame): Dataset containing 'group' and 'conversion' columns.

    Returns:
        None
    """
    # Bar plot for conversion rates
    conversion_rates = data.groupby("group")["conversion"].mean().reset_index()
    sns.barplot(x="group", y="conversion", data=conversion_rates, ci=None)
    plt.title("Conversion Rates by Group")
    plt.ylabel("Conversion Rate")
    plt.show()

    # Histogram of conversions
    sns.histplot(data, x="conversion", hue="group", multiple="dodge", shrink=0.8)
    plt.title("Histogram of Conversions by Group")
    plt.xlabel("Conversion")
    plt.show()

# Example usage
if __name__ == "__main__":
    import pandas as pd
    from data_simulation import simulate_data

    # Simulate data and visualize
    data = simulate_data()
    visualize_data(data)