import numpy as np


def predict(model, features):
    """
    Run model inference on input features.
    """
    data = np.array(features).reshape(1, -1)
    prediction = model.predict(data)
    return int(prediction[0])