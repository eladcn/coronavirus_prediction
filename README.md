# Coronavirus (COVID-19) Prediction
This project aims to predict the numbers that are published in each day regarding the amount of Coronavirus (COVID-19) cases and deaths.

## Requirements
1. A machine with Python 3 installed.
2. The following packages are needed to be installed for this project to run:
    - numpy
    - matplotlib
    - scikit-learn
    - BeautifulSoup

## How to use
1. Install the required packages (as mentioned above).
2. Run the main.py file using Python 3.

## How does it work?
The main.py file uses the DataGrabber class (source included) to fetch the required data from https://www.worldometers.info.  
The main.py file then trains 2 models using the fetched data and scikit-learn's LinearRegression - the cases in each day model  
and then the deaths in each day model.  
Afterwards, the file displays the models' predictions for the next day, the functions that depict the trained models and displays a graph for each model.

## Output examples
### Terminal output
![Terminal output](/outputs/terminal.png)

### Cases in each day graph
![Cases in each day graph](/outputs/cases_in_each_day.svg)

### Deaths in each day graph
![Deaths in each day graph](/outputs/deaths_in_each_day.svg)

## Predictions
| Date       | Cases  | Deaths | Predicted Cases | Predicted Deaths | Notes                                                    |
| ---------- | ------ | ------ | --------------- | ---------------- | -------------------------------------------------------- |
| 22.02.2020 | TBA    | TBA    | 80,423          | 2,458            | Changed the cases model polynomial degree.               |
| 21.02.2020 | 77,912 | 2,360  | 75,162          | 2,355            | We need more cases data in order to have correct values. |
| 20.02.2020 | 76,806 | 2,247  | 76,109          | 2,248            | The data for previous days was changed in this day.      |
| 19.02.2020 | 75,700 | 2,126  | 77,427          | 2,138            |                                                          |
| 18.02.2020 | 75,184 | 2,009  | 77,842          | 2,030            | Changed the polynomials degrees.                         |
| 17.02.2020 | 73,332 | 1,873  | 79,231          | 1,956            |                                                          |
| 16.02.2020 | 71,329 | 1,775  | 76,943          | 1,824            |                                                          |
| 15.02.2020 | 69,197 | 1,669  | 73,331          | 1,668            |                                                          |
| 14.02.2020 | 67,100 | 1,526  | 67,496          | 1,516            |                                                          |
| 13.02.2020 | 64,438 | 1,383  | 58,692          | 1,376            |                                                          |
| 12.02.2020 | 45,134 | 1,261  | 48,123          | 1,233            |                                                          |
