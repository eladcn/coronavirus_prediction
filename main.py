import operator
import json
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

from data_grabbers.cases_data_grabber import CasesDataGrabber
from data_grabbers.deaths_data_grabber import DeathsDataGrabber

def grab_training_set(datagrabber_class, grab_data_from_server=True, offline_dataset_date=""):
    grabber = globals()[datagrabber_class]()
    dataset_date = ""

    if grab_data_from_server:
        grabber.grab_data()
    else:
        dataset_date = offline_dataset_date

        if offline_dataset_date == "":
            raise Exception("Invalid offline dataset date received. Please update the 'offline_dataset_date' configuration in the config file and try again.")
    
    filename = grabber.get_dataset_file_name(dataset_date=dataset_date)

    return np.genfromtxt("datasets/" + filename, delimiter=',').astype(np.int32)

def train_model(x, y, polynomial_degree):
    polynomial_features = PolynomialFeatures(degree=polynomial_degree)
    x_poly = polynomial_features.fit_transform(x)

    model = LinearRegression()
    model.fit(x_poly, y)

    return model

def get_predictions(x, model, polynomial_degree):
    polynomial_features = PolynomialFeatures(degree=polynomial_degree)
    x_poly = polynomial_features.fit_transform(x)

    return model.predict(x_poly)

def print_stats(model_name, model, x, y, polynomial_degree, days_to_predict):
    y_pred = np.round(get_predictions(x, model, polynomial_degree), 0).astype(np.int32)

    print_forecast(model_name, model, polynomial_degree, beginning_day=len(x), limit=days_to_predict)
    print_model_polynomial(model_name, model)
    plot_graph(model_name, x, y, y_pred)
    print("")

def print_model_polynomial(model_name, model):
    coef = model.coef_
    intercept = model.intercept_
    poly = "{0:.3f}".format(intercept)

    for i in range(1, len(coef)):
        if coef[i] >= 0:
            poly += " + "
        else:
            poly += " - "
        
        poly += "{0:.3f}".format(coef[i]).replace("-", "") + "X^" + str(i)

    print("The " + model_name + " model function is: f(X) = " + poly)

def plot_graph(model_name, x, y, y_pred):
    plt.scatter(x, y, s=10)
    sort_axis = operator.itemgetter(0)
    sorted_zip = sorted(zip(x, y_pred), key=sort_axis)
    x, y_pred = zip(*sorted_zip)
    
    plt.plot(x, y_pred, color='m')
    plt.title("Amount of " + model_name + " in each day")
    plt.xlabel("Day")
    plt.ylabel(model_name)
    plt.show()

def print_forecast(model_name, model, polynomial_degree, beginning_day=0, limit=10):
    next_days_x = np.array(range(beginning_day, beginning_day + limit)).reshape(-1, 1)
    next_days_pred = np.round(get_predictions(next_days_x, model, polynomial_degree), 0).astype(np.int32)

    print("The forecast for " + model_name + " in the following " + str(limit) + " days is:")

    for i in range(0, limit):
        print(str(i + 1) + ": " + str(next_days_pred[i]))

def model_handler(model_config):
    training_set = grab_training_set(model_config["datagrabber_class"], model_config["grab_data_from_server"], model_config["offline_dataset_date"])
    x = training_set[:, 0].reshape(-1, 1)
    y = training_set[:, 1]
    model = train_model(x, y, model_config["polynomial_degree"])

    print_stats(model_config["model_name"], model, x, y, model_config["polynomial_degree"], model_config["days_to_predict"])

if __name__ == "__main__":
    config = {}

    with open("config.json", "r") as f:
        config = json.load(f)

    for model_config in config["models"]:
        model_handler(model_config)
