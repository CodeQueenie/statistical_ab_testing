from scipy.stats import chi2_contingency, norm
import pandas as pd

def z_test_proportion(group_a, group_b):
    """
    Perform a Z-test for proportions between two groups.

    Args:
        group_a (pd.Series): Conversions for group A.
        group_b (pd.Series): Conversions for group B.

    Returns:
        float, float: Z-score and p-value.
    """
    n_a, n_b = len(group_a), len(group_b)
    p_a, p_b = group_a.mean(), group_b.mean()
    p_pool = (group_a.sum() + group_b.sum()) / (n_a + n_b)
    z_score = (p_a - p_b) / ((p_pool * (1 - p_pool) * (1 / n_a + 1 / n_b)) ** 0.5)
    p_value = 2 * (1 - norm.cdf(abs(z_score)))
    return z_score, p_value

def chi_square_test(data):
    """
    Perform a Chi-Square test on the dataset.

    Args:
        data (pd.DataFrame): Dataset containing 'group' and 'conversion' columns.

    Returns:
        float, float: Chi-Square statistic and p-value.
    """
    contingency_table = pd.crosstab(data["group"], data["conversion"])
    chi2, p, _, _ = chi2_contingency(contingency_table)
    return chi2, p

# Example usage
if __name__ == "__main__":
    from data_simulation import simulate_data

    # Simulate data
    data = simulate_data()

    # Split into groups
    group_a = data[data["group"] == "A"]["conversion"]
    group_b = data[data["group"] == "B"]["conversion"]

    # Perform Z-test
    z_score, p_value = z_test_proportion(group_a, group_b)
    print(f"Z-Test: Z-Score = {z_score:.4f}, P-Value = {p_value:.4f}")

    # Perform Chi-Square test
    chi2, p_value_chi2 = chi_square_test(data)
    print(f"Chi-Square Test: Chi2 = {chi2:.4f}, P-Value = {p_value_chi2:.4f}")