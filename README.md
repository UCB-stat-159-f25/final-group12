# NBA Player Salary Analysis (2024-2025 Season)
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/sSkqmNLf)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-f25/final-group12/main)
## Project Description
This project analyzes the determinants of NBA player salaries using data from the 2024-2025 regular season. We investigate how traditional statistics, advanced metrics, age, and position influence player compensation, with particular attention to the impact of superstar salaries on overall patterns. The analysis combines regularized linear regression with ensemble methods to provide a comprehensive view of salary determinants in professional basketball.

## Motivation
NBA salaries exhibit extreme skew, with a small number of superstars earning significantly more than average players. This project seeks to understand which performance metrics teams value when determining compensation, whether traditional box score statistics or advanced all-in-one metrics better predict salary, and how these relationships change when examining different segments of the player population.

## Analysis Overview
We implement the following modeling approaches to analyze 2024-2025 NBA salary data:

1. Ordinary Least Squares regression as a baseline
1. Ridge and LASSO regression to handle correlated predictors
1. Random Forest and Gradient Boosting for non-linear patterns and feature importance
