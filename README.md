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

### Handling Null Values
You can handle null values in your dataset using various strategies with the handle_null_values method. Supported strategies include:

* 'drop': Drops rows with any null values.
* 'fill_median': Fills null values with column medians.
* 'fill_mean': Fills null values with column means.
* 'interpolate': Interpolates missing values using linear interpolation.
Here's how to use it:
```python   
# Handle null values using different strategies
cleaned_data_drop = my_tools.handle_null_values(strategy='drop')
cleaned_data_fill_median = my_tools.handle_null_values(strategy='fill_median')
cleaned_data_fill_mean = my_tools.handle_null_values(strategy='fill_mean')
cleaned_data_interpolate = my_tools.handle_null_values(strategy='interpolate')
```
### Contributing
Contributions are welcome! If you have any improvements or new features to add, please submit a pull request.


### License
This project is licensed under the MIT License - see the LICENSE file for details.
Check my other projects here : 
    
