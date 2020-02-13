import operator
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

from data_grabber import DataGrabber

CASES_POLYNOMIAL_DEGREE = 5
DEATHS_POLYNOMIAL_DEGREE = 5
GRAB_DATA_FILE_FROM_SERVER = True # Set this to False if you already have the data and you don't wish to redownload it.

def get_training_set_from_file(dataset_type):
    filename = DataGrabber().get_dataset_file_name(dataset_type=dataset_type)

    return np.genfromtxt("datasets/" + filename, delimiter=',').astype(np.int32)

def get_training_sets():
    grabber = DataGrabber()

    if GRAB_DATA_FILE_FROM_SERVER:
        grabber.grab_data()
    
    return (get_training_set_from_file("cases"), get_training_set_from_file("deaths"))

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
    (training_set_cases, training_set_deaths) = get_training_sets()
    x_cases = training_set_cases[:, 0].reshape(-1, 1)
    x_deaths = training_set_deaths[:, 0].reshape(-1, 1)
    y_cases = training_set_cases[:, 1]
    y_deaths = training_set_deaths[:, 1]

    cases_model = train_model(x_cases, y_cases, CASES_POLYNOMIAL_DEGREE)
    deaths_model = train_model(x_deaths, y_deaths, DEATHS_POLYNOMIAL_DEGREE)

    print_stats("Cases", cases_model, x_cases, y_cases, CASES_POLYNOMIAL_DEGREE)
    print_stats("Deaths", deaths_model, x_deaths, y_deaths, DEATHS_POLYNOMIAL_DEGREE)
