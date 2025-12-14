import numpy as np

def mse_func(predictions, actual):
    diff = predictions - actual
    squared = diff ** 2
    summed = np.sum(squared)
    n = len(predictions)
    return (1/n) * summed

def split_train_test(X, y, train_size, seed):
    np.random.seed(42)
    n = len(y)
    split = int(np.round(train_size * n))
    perm = np.random.permutation(n)
    X_train = X.iloc[perm].iloc[:split]
    y_train = y.iloc[perm].iloc[:split]
    X_test = X.iloc[perm].iloc[split:]
    y_test = y.iloc[perm].iloc[split:]

    return X_train, X_test, y_train, y_test
    