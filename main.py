import operator
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

from data_grabber import DataGrabber

CASES_POLYNOMIAL_DEGREE = 5
DEATHS_POLYNOMIAL_DEGREE = 4
GRAB_DATA_FILE_FROM_SERVER = True
DEFAULT_DATA_FILE_NAME = "dataset_2020-02-11.csv" # This will be used as the data file if GRAB_DATA_FILE_FROM_SERVER is set to False.

def get_training_set():
    grabber = DataGrabber()
    data_file_name = DEFAULT_DATA_FILE_NAME

    if GRAB_DATA_FILE_FROM_SERVER:
        grabber.grab_data()
        data_file_name = grabber.get_default_file_name()
    
    return np.genfromtxt("datasets/" + data_file_name, delimiter=',').astype(np.int32)

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

def print_stats(model_name, model, x, y, polynomial_degree):
    y_pred = np.round(get_predictions(x, model, polynomial_degree), 0).astype(np.int32)
    next_day_x = np.array([len(x)]).reshape(-1, 1)
    next_day_pred = np.round(get_predictions(next_day_x, model, polynomial_degree), 0)

    print_model_polynomial(model_name, model)
    print("The predicted amount of " + model_name + " in the next day is: " + str(int(next_day_pred)))

    rmse = np.sqrt(mean_squared_error(y, y_pred))
    r2 = r2_score(y, y_pred)

    print(model_name + " RMSE: " + str(rmse))
    print(model_name + " R2: " + str(r2))
    print("")

    plot_graph(model_name, x, y, y_pred)

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

    print("The " + model_name + " function is: f(X) = " + poly)

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

if __name__ == "__main__":
    training_set = get_training_set()
    x = training_set[:, 0].reshape(-1, 1)
    y_cases = training_set[:, 1]
    y_deaths = training_set[:, 2]

    cases_model = train_model(x, y_cases, CASES_POLYNOMIAL_DEGREE)
    deaths_model = train_model(x, y_deaths, DEATHS_POLYNOMIAL_DEGREE)

    print_stats("Cases", cases_model, x, y_cases, CASES_POLYNOMIAL_DEGREE)
    print_stats("Deaths", deaths_model, x, y_deaths, DEATHS_POLYNOMIAL_DEGREE)
