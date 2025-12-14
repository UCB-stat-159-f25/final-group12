import pytest
from functions import mse_func
from functions import split_train_test
import numpy as np
import pandas as pd

def test_mse():
    predictions = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    actual = np.array([11, 3, 7, 2, 15, 1, 0, 0, 6, 3])

    mse = mse_func(predictions, actual)

    assert mse == 41.7

def test_split_train_test():
    df = pd.DataFrame({
        'col1': ['a', 'b', 'c', 'd', 'e'],
        'col2': ['A', 'B', 'C', 'D', 'E'],
        'col3': ['1', '2', '3', '4', '5'],
        'col4': ['11', '22', '33', '44', '55'],
        'col5': ['red', 'orange', 'yellow', 'green', 'blue']
    })

    y =pd.Series(['y1', 'y2', 'y3', 'y4', 'y5'])

    X_train, X_test, y_train, y_test = split_train_test(df, y, 0.8, 42)

    assert len(X_train) == 4
    assert len(y_train) == 4
    assert len(X_test) == 1
    assert len(y_test) == 1