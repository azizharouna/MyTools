# MyTools - A Python Mother Class for Data Analysis

MyTools is a Python class designed to simplify common data analysis tasks. It includes methods for outlier detection and handling null values using various strategies. This README provides an overview of the class and its usage.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Outlier Detection](#outlier-detection)
  - [Handling Null Values](#handling-null-values)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Installation

You can use MyTools by simply including it in your Python project or importing it into your script.

```python
from mytools import MyTools
``` 

## Usage
### Outlier Detection
MyTools provides a method for outlier detection using Scikit-Learn's Robust Covariance Estimation and Mahalanobis distance. Here's how to use it:

```python
# Create an instance of MyTools with your data
my_tools = MyTools(your_dataframe)

# Detect outliers and return cleaned data (default)
cleaned_data = my_tools.robust_mahalanobis_outlier_detection()

# Detect outliers and return only outliers
outliers = my_tools.robust_mahalanobis_outlier_detection(return_outliers=True)

``` 

    
