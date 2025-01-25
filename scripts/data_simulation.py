import pandas as pd
import numpy as np

def simulate_data(size_a=1000, size_b=1000, conv_rate_a=0.10, conv_rate_b=0.12, random_seed=42):
    """
    Simulate data for A/B testing with specified sample sizes and conversion rates.

    Args:
        size_a (int): Number of samples in group A.
        size_b (int): Number of samples in group B.
        conv_rate_a (float): Conversion rate for group A.
        conv_rate_b (float): Conversion rate for group B.
        random_seed (int): Seed for reproducibility.

    Returns:
        pd.DataFrame: Simulated dataset for both groups.
    """
    np.random.seed(random_seed)  # Set the random seed

    group_a = pd.DataFrame({
        "user_id": range(1, size_a + 1),
        "group": "A",
        "conversion": np.random.choice([0, 1], size=size_a, p=[1 - conv_rate_a, conv_rate_a])
    })
    group_b = pd.DataFrame({
        "user_id": range(size_a + 1, size_a + size_b + 1),
        "group": "B",
        "conversion": np.random.choice([0, 1], size=size_b, p=[1 - conv_rate_b, conv_rate_b])
    })
    return pd.concat([group_a, group_b], ignore_index=True)