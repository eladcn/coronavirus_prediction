# Coronavirus (COVID-19) Prediction
This project aims to predict the numbers that are published in each day regarding the amount of Coronavirus (COVID-19) cases and deaths.

## Table of contents
- [Requirements](#requirements)
- [How to use](#how-to-use)
- [How does it work](#how-does-it-work)
- [Contact info](#contact-info)
- [Output examples](#output-examples)
    * [Terminal output](#terminal-output)
    * [Cases in each day graph](#cases-in-each-day-graph)
    * [Deaths in each day graph](#deaths-in-each-day-graph)
- [Predictions](#predictions)

## Requirements
1. A machine with Python 3 installed.
2. The following packages are needed to be installed for this project to run:
    - numpy
    - matplotlib
    - scikit-learn
    - BeautifulSoup

## How to use
(Using Poetry)
1. Install [Poetry](https://python-poetry.org/)
2. Run `poetry install`
3. Run `poetry run python main.py`

(Not using Poetry)
1. Install dependencies with `pip install -r requirements.txt`
2. Run `python main.py`

## How does it work
The main.py file uses the DataGrabber class (source included) to fetch the required data from https://www.worldometers.info.  
The main.py file then trains 2 polynomial models using the fetched data and scikit-learn's LinearRegression - the cases in each day model and then the deaths in each day model.  
Afterwards, the file displays the models' predictions for the next day, the functions that depict the trained models and displays a graph for each model.

## Contact info
You may contact me via Linkedin: https://www.linkedin.com/in/eladcn/.

## Output examples
### Terminal output
![Terminal output](/outputs/terminal.png)

### Cases in each day graph
![Cases in each day graph](/outputs/cases_in_each_day.svg)

### Deaths in each day graph
![Deaths in each day graph](/outputs/deaths_in_each_day.svg)

## Predictions
| Date       | Cases     | Deaths | Predicted Cases | Predicted Deaths | Notes                                                    |
| ---------- | --------- | ------ | --------------- | ---------------- | -------------------------------------------------------- |
| 03.04.2020 | TBA       | TBA    | 1,101,907       | 58,909           | Restored the deaths model's polynomial degree.           |
| 02.04.2020 | 1,015,065 | 53,167 | 1,023,706       | 52,199           | Changed the models' poloynomials degrees.                |
| 01.04.2020 | 935,197   | 47,192 | 965,240         | 47,590           |                                                          |
| 31.03.2020 | 858,355   | 42,309 | 885,894         | 42,849           |                                                          |
| 30.03.2020 | 784,794   | 37,788 | 810,279         | 38,570           |                                                          |
| 29.03.2020 | 722,359   | 33,966 | 734,545         | 34,636           |                                                          |
| 28.03.2020 | 663,124   | 30,862 | 657,417         | 30,684           |                                                          |
| 27.03.2020 | 596,366   | 27,344 | 585,678         | 27,119           |                                                          |
| 26.03.2020 | 531,865   | 24,073 | 521,527         | 23,997           |                                                          |
| 25.03.2020 | 471,035   | 21,284 | 466,864         | 21,207           |                                                          |
| 24.03.2020 | 422,599   | 18,894 | 417,312         | 18,651           |                                                          |
| 23.03.2020 | 378,860   | 16,514 | 372,656         | 16,494           |                                                          |
| 22.03.2020 | 337,469   | 14,647 | 334,355         | 14,544           |                                                          |
| 21.03.2020 | 305,036   | 13,013 | 298,845         | 12,760           |                                                          |
| 20.03.2020 | 275,598   | 11,387 | 265,940         | 11,271           |                                                          |
| 19.03.2020 | 244,933   | 10,031 | 239,006         | 10,027           |                                                          |
| 18.03.2020 | 218,822   | 8,951  | 217,680         | 8,934            |                                                          |
| 17.03.2020 | 198,234   | 7,978  | 200,305         | 8,009            |                                                          |
| 16.03.2020 | 182,473   | 7,160  | 184,930         | 7,223            |                                                          |
| 15.03.2020 | 169,577   | 6,519  | 170,336         | 6,504            |                                                          |
| 14.03.2020 | 156,622   | 5,833  | 157,620         | 5,966            |                                                          |
| 13.03.2020 | 145,483   | 5,429  | 146,450         | 5,434            |                                                          |
| 12.03.2020 | 134,577   | 4,982  | 137,917         | 4,984            |                                                          |
| 27.02.2020 | 83,113    | 2,858  | -               | 2,867            |                                                          |
| 26.02.2020 | 81,828    | 2,801  | -               | 2,839            |                                                          |
| 25.02.2020 | 80,828    | 2,763  | -               | 2,775            |                                                          |
| 24.02.2020 | 80,087    | 2,699  | -               | 2,679            | The cases model needs to be changed.                     |
| 23.02.2020 | 79,205    | 2,618  | 79,611          | 2,548            |                                                          |
| 22.02.2020 | 78,651    | 2,460  | 80,423          | 2,458            | Changed the cases model polynomial degree.               |
| 21.02.2020 | 77,673    | 2,360  | 75,162          | 2,355            | We need more cases data in order to have correct values. |
| 20.02.2020 | 76,667    | 2,247  | 76,109          | 2,248            | The data for previous days was changed in this day.      |
| 19.02.2020 | 75,700    | 2,126  | 77,427          | 2,138            |                                                          |
| 18.02.2020 | 75,184    | 2,009  | 77,842          | 2,030            | Changed the polynomials degrees.                         |
| 17.02.2020 | 73,332    | 1,873  | 79,231          | 1,956            |                                                          |
| 16.02.2020 | 71,329    | 1,775  | 76,943          | 1,824            |                                                          |
| 15.02.2020 | 69,197    | 1,669  | 73,331          | 1,668            |                                                          |
| 14.02.2020 | 67,100    | 1,526  | 67,496          | 1,516            |                                                          |
| 13.02.2020 | 64,438    | 1,383  | 58,692          | 1,376            |                                                          |
| 12.02.2020 | 45,134    | 1,261  | 48,123          | 1,233            |                                                          |
