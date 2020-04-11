import numpy as np

from sklearn.neural_network import MLPRegressor

class NeuralNetModel:
    def __init__(self, model_name):
        self.__model_name = model_name
        self.__model = None

    def train(self, x, y, hidden_layer_sizes=[10,], learning_rate=0.001, max_iter=2000):
        self.__model = MLPRegressor(solver="adam", activation="relu", alpha=1e-5, random_state=0, hidden_layer_sizes=hidden_layer_sizes, verbose=False, tol=1e-5, learning_rate_init=learning_rate, max_iter=max_iter)
        self.__model.fit(x, y)

    def get_predictions(self, x):
        return np.round(self.__model.predict(x), 0).astype(np.int32)
