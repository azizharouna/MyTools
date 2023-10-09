import numpy as np
import pandas as pd
from sklearn.covariance import EllipticEnvelope
from scipy.spatial.distance import mahalanobis




class MyTools:
    def __init__(self, data):
        self.data = data

    def robust_mahalanobis_outlier_detection(self, contamination=0.1, return_outliers=False):
        """
        Detect outliers using Robust Covariance Estimation and Mahalanobis distance.
        
        Args:
            contamination (float): The proportion of outliers to expect in the data.
            return_outliers (bool): If True, return a dataset of only outliers; otherwise, return a cleaned dataset.
        
        Returns:
            pd.DataFrame: Cleaned DataFrame (default) or DataFrame of outliers.
        """
        # Fit the robust covariance estimator
        robust_cov = EllipticEnvelope(contamination=contamination)
        robust_cov.fit(self.data)

        # Compute the Mahalanobis distances
        mahal_dist = robust_cov.mahalanobis(self.data)

        # Set a threshold for outlier detection
        threshold = np.percentile(mahal_dist, 100 * (1 - contamination))

        if return_outliers:
            # Return only the outliers
            outliers = self.data[mahal_dist > threshold]
            return outliers
        else:
            # Return a cleaned dataset (excluding outliers)
            cleaned_data = self.data[mahal_dist <= threshold]
            return cleaned_data
        
    def handle_null_values(self, strategy='drop'):
        """
        Handle null values in the dataset based on the chosen strategy.

        Args:
            strategy (str): Strategy to handle null values. Options: 'drop', 'fill_median', 'fill_mean', 'interpolate'.

        Returns:
            pd.DataFrame: Cleaned DataFrame after handling null values.
        """
        if strategy == 'drop':
            # Drop rows with any null values
            cleaned_data = self.data.dropna()
        elif strategy == 'fill_median':
            # Fill null values with the median of each column
            cleaned_data = self.data.fillna(self.data.median())
        elif strategy == 'fill_mean':
            # Fill null values with the mean of each column
            cleaned_data = self.data.fillna(self.data.mean())
        elif strategy == 'interpolate':
            # Interpolate missing values using linear interpolation
            cleaned_data = self.data.interpolate(method='linear', axis=0)
        else:
            raise ValueError("Invalid strategy. Choose from 'drop', 'fill_median', 'fill_mean', or 'interpolate'.")

        return cleaned_data

# Example usage:
if __name__ == "__main__":
    # Sample DataFrame
    data = pd.DataFrame({
        'Feature1': [1.0, 2.0, 3.0, np.nan, 5.0, 100.0],
        'Feature2': [10.0, 20.0, np.nan, 40.0, 50.0, 1000.0]
    })

    # Create an instance of MyTools
    my_tools = MyTools(data)

    # Handle null values using different strategies
    cleaned_data_drop = my_tools.handle_null_values(strategy='drop')
    cleaned_data_fill_median = my_tools.handle_null_values(strategy='fill_median')
    cleaned_data_fill_mean = my_tools.handle_null_values(strategy='fill_mean')
    cleaned_data_interpolate = my_tools.handle_null_values(strategy='interpolate')

    print("Cleaned Data (Drop Nulls):")
    print(cleaned_data_drop)

    print("\nCleaned Data (Fill with Median):")
    print(cleaned_data_fill_median)

    print("\nCleaned Data (Fill with Mean):")
    print(cleaned_data_fill_mean)

    print("\nCleaned Data (Interpolate):")
    print(cleaned_data_interpolate)