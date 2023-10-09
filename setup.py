from setuptools import setup, find_packages

setup(
    name='mytools',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'statsmodels'
    ],
    author='Abdoul Aziz Moussa',
    author_email='abdoulenergy@gmail.com',
    description='A Python Mother Class for Data Analysis',
    license='MIT',
)
