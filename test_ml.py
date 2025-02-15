import pytest
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.data import apply_label
from ml.model import train_model, compute_model_metrics

def test_apply_labels():
    """
    Test if apply_label function returns expected string values
    """
    assert apply_label([1]) == ">50K"
    assert apply_label([0]) == "<=50K"

def test_train_model():
    """
    Test if train_model returns a RandomForestClassifier and can make predictions
    """
    X = np.array([[1, 2], [3, 4]])
    y = np.array([0, 1])
    model = train_model(X, y)
    
    # Check if model is correct type
    assert isinstance(model, RandomForestClassifier)
    
    # Check if model can make predictions
    pred = model.predict(X)
    assert len(pred) == len(y)

def test_compute_model_metrics():
    """
    Test if compute_model_metrics returns expected values for perfect predictions
    """
    y = np.array([0, 0, 1, 1])
    preds = np.array([0, 0, 1, 1])
    
    precision, recall, fbeta = compute_model_metrics(y, preds)
    assert precision == 1.0
    assert recall == 1.0 
    assert fbeta == 1.0