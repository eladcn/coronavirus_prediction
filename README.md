# Coronavirus (2019-nCoV) Prediction
This project aims to predict the numbers that are published in each day regarding the amount of Coronavirus (2019-nCoV) cases and deaths.

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
Afterwards, the file displays the models' predictions for the next day, as well as statistics about the models (the RMSE and R2 values), displays a graph for each model that shows how well they score and the functions that depict the trained model.

## Output examples
### Terminal output
![Terminal output](/outputs/terminal.png)

### Cases in each day graph
![Cases in each day graph](/outputs/cases_in_each_day.svg)

### Deaths in each day graph
![Deaths in each day graph](/outputs/deaths_in_each_day.svg)
