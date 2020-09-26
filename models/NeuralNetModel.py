import numpy as np
import copy

from sklearn.neural_network import MLPRegressor

class NeuralNetModel:
    KEYS_TO_REMOVE = ["_comment", "type"]

    def __init__(self, model_name):
        self.__model_name = model_name
        self.__model = None

    def train(self, x, y, config):
        config = copy.deepcopy(config)
        config["hidden_layer_sizes"] = self.calc_hidden_layer(x, config.get("hidden_layer_sizes", "auto"))

        for key in NeuralNetModel.KEYS_TO_REMOVE:
            if key in config:
                del config[key]
        
        self.__model = MLPRegressor(**config)
        self.__model.fit(x, y)

    def calc_hidden_layer(self, x, hidden_layer_sizes="auto"):
        if (hidden_layer_sizes != "auto"):
            return hidden_layer_sizes
        
        calculated = int(len(x) / 5)

        return [calculated, calculated]

    def get_predictions(self, x):
        return np.round(self.__model.predict(x), 0).astype(np.int32)
