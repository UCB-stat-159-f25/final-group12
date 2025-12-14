# NBA Player Salary Analysis (2024-2025 Season)
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/sSkqmNLf)
Main Repo:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/final-group12/main)
## Project Description
This project analyzes the determinants of NBA player salaries using data from the 2024-2025 regular season. We investigate how traditional statistics, advanced metrics, age, and position influence player compensation, with particular attention to the impact of superstar salaries on overall patterns. The analysis combines regularized linear regression with ensemble methods to provide a comprehensive view of salary determinants in professional basketball.

## Motivation
NBA salaries exhibit extreme skew, with a small number of superstars earning significantly more than average players. This project seeks to understand which performance metrics teams value when determining compensation, whether traditional box score statistics or advanced all-in-one metrics better predict salary.

We implement the following modeling approaches to analyze 2024-2025 NBA salary data:

1. Ordinary Least Squares regression as a baseline
1. Ridge and LASSO regression to handle correlated predictors
1. Random Forest for non-linear patterns and feature importance

## Repository Structure

The repository is structured as follows:

* `data/`: Contains the raw dataset and processed data files
* `outputs/`: Contains the generated figures and plots
* `nba_scraper/`: Contains utility functions used to scrape data from BasketballReference
* `modeling_functions`: Contains utility functions for modeling stats against player salary
* `main.ipynb`: Main project notebook, providing an overview of the analysis and results
* `data_scraping.ipynb`: Notebook containing data scraping and cleaning
* `feature_engineering.ipynb`: Notebook containing data preprocessing and feature engineering
* `eda.ipynb`: Notebook containing exploratory data analysis
* `modeling.ipynb`: Notebook containing model training, evaluation, and interpretation
* `environment.yml`: Environment file with required packages for the project
* `Makefile`: Makefile to build MyST website for the repository and manage other tasks

## Setup and Installation

1. Clone this repository:
```python
git clone https://github.com/UCB-stat-159-f25/final-group12.git
cd final-group12
```
2. Create and activate the nba conda environment:
```python
make env
conda activate nba
```
3. Install the IPython kernel with the nba environment:
```python
python -m ipykernel install --user --name nba --display-name "IPython - nba"
```

4. Feel free to run our notebooks to reproduce our analysis!
Data Scraping:[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/final-group12/main?labpath=data_scraping.ipynb)
Feature Engineering:[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/final-group12/main?labpath=feature_engineering.ipynb)
EDA:[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/final-group12/main?labpath=eda.ipynb)
Modeling:[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/final-group12/main?labpath=modeling.ipynb)
Main Results:[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/final-group12/main?labpath=main.ipynb)

## Testing
To run tests on our utility functions, navigate to the root directory of the project and execute the following command:
	
	PYTHONPATH=./ pytest

## Overall Results
For overall information about the analysis and results, please refer to the main.ipynb notebook.
