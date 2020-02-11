import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

""" 
This class handles grabbing the data regarding CCP's coronavirus confirmed cases and deaths from the website:
https://www.worldometers.info
"""
class DataGrabber:
    TARGET_DOMAIN = "https://www.worldometers.info"

    def grab_data(self, filename=''):
        cases = self.get_cases()
        deaths = self.get_deaths()

        if filename == '':
            filename = self.get_default_file_name()

        self.save_data_to_file(filename, cases, deaths)

    def get_cases(self):
        cases_url = DataGrabber.TARGET_DOMAIN + "/coronavirus/coronavirus-cases/"
        cases_request = requests.get(cases_url)
        cases_content = cases_request.content

        cases_soup = BeautifulSoup(cases_content, "html.parser")

        cases = []
        cases_table = cases_soup.select(".table-responsive")[2].find("table")
        cases_table_rows = cases_table.select("tr")

        for i in range(1, len(cases_table_rows)):
            current_cases = int(cases_table_rows[i].find_next("td").find_next("td").string.replace(",", ""))
            cases.append(current_cases)

        return list(reversed(cases))
    
    def get_deaths(self):
        deaths_url = DataGrabber.TARGET_DOMAIN + "/coronavirus/coronavirus-death-toll/"
        deaths_request = requests.get(deaths_url)
        deaths_content = deaths_request.content

        deaths_soup = BeautifulSoup(deaths_content, "html.parser")

        deaths = []
        deaths_table = deaths_soup.select(".table-responsive")[0].find("table")
        deaths_table_rows = deaths_table.select("tr")

        for i in range(1, len(deaths_table_rows)):
            current_deaths = int(deaths_table_rows[i].find_next("td").find_next("td").string.replace(",", ""))
            deaths.append(current_deaths)

        return list(reversed(deaths))

    def save_data_to_file(self, filename, cases, deaths):
        data = []

        for i in range(0, len(cases)):
            data.append([i, cases[i], deaths[i]])
        
        with open("datasets/" + filename, 'w', newline='') as f:
            csv_writer = csv.writer(f, delimiter=',')
            csv_writer.writerows(data)

    def get_default_file_name(self):
        return "dataset_" + datetime.today().strftime('%Y-%m-%d') + ".csv"