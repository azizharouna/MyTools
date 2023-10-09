import numpy as np
import pandas as pd
from sklearn.covariance import EllipticEnvelope
from scipy.spatial.distance import mahalanobis
from statsmodels.stats.outliers_influence import variance_inflation_factor




class MyTools:
    def __init__(self, data, features=None):
        self.data = data
        if features is None:
            # If no features are provided, use all numeric columns as features
            self.features = data.select_dtypes(include=['number'])
        else:
            self.features = features

    def robust_mahalanobis_outlier_detection(self, contamination=0.1, return_outliers=False):
        """
        Detect outliers using Robust Covariance Estimation and Mahalanobis distance.
        
        Args:
            contamination (float): The proportion of outliers to expect in the data.
            return_outliers (bool): If True, return a dataset of only outliers; otherwise, return a cleaned dataset.
        
        Returns:
            pd.DataFrame: Cleaned DataFrame (default) or DataFrame of outliers.
        """
        # Select only the numeric columns for Mahalanobis distance calculation
        numeric_data = self.features.select_dtypes(include=['number'])

        
        # Fit the robust covariance estimator
        robust_cov = EllipticEnvelope(contamination=contamination)
        robust_cov.fit(numeric_data)

         # Compute the Mahalanobis distances
        mahal_dist = robust_cov.mahalanobis(numeric_data)

        
        # Set a threshold for outlier detection
        threshold = np.percentile(mahal_dist, 100 * (1 - contamination))

         # Fit the robust covariance estimator
        robust_cov = EllipticEnvelope(contamination=contamination)
        robust_cov.fit(numeric_data)
        

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
        
    

    
    def check_collinearity(self, threshold=5.0):
        """
        Check for collinearity among features using Variance Inflation Factor (VIF).

        Args:
            threshold (float): The threshold value for VIF. Features with VIF greater than this value are considered collinear.

        Returns:
            pd.DataFrame: DataFrame showing VIF for each feature.
        """
        # Filter the features DataFrame to include only numeric columns
        numeric_features = self.features.select_dtypes(include=['number'])

        # Calculate VIF for numeric features
        vif_data = pd.DataFrame()
        vif_data["Feature"] = numeric_features.columns
        vif_data["VIF"] = [variance_inflation_factor(numeric_features.values, i) for i in range(numeric_features.shape[1])]

        # Filter features with VIF above the threshold
        collinear_features = vif_data[vif_data["VIF"] > threshold]

        return vif_data, collinear_features


