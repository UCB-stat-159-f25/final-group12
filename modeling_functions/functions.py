import numpy as np

def mse_func(predictions, actual):
    """
    Calculate the Mean Squared Error (MSE) between predictions and actual values.
    
    Parameters
    ----------
    predictions : array-like
        Array or list of predicted values from a regression model.
    actual : array-like
        Array or list of actual observed values, must have same length as predictions.
        
    Returns
    -------
    float
        The mean squared error calculated as (1/n) * the sum of the squared difference between actual and the predictions.
    """
    diff = predictions - actual
    squared = diff ** 2
    summed = np.sum(squared)
    n = len(predictions)
    return (1/n) * summed

def split_train_test(X, y, train_size, seed):
    """
    Split feature and target data into training and testing sets with random shuffling.
    
    Parameters
    ----------
    X : pandas.DataFrame or array-like
        Feature matrix or DataFrame containing predictor variables.
    y : pandas.Series or array-like
        Target vector containing the response variable, must have same length as X.
    train_size : float
        Proportion of data to include in the training split (between 0 and 1).
    seed : int
        Random seed for reproducible shuffling and splitting.
        
    Returns
    -------
    tuple of (X_train, X_test, y_train, y_test)
        X_train : Training features
        X_test : Testing features  
        y_train : Training targets
        y_test : Testing targets
    """
    np.random.seed(42)
    n = len(y)
    split = int(np.round(train_size * n))
    perm = np.random.permutation(n)
    X_train = X.iloc[perm].iloc[:split]
    y_train = y.iloc[perm].iloc[:split]
    X_test = X.iloc[perm].iloc[split:]
    y_test = y.iloc[perm].iloc[split:]

    return X_train, X_test, y_train, y_test
    