import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

""" 
This class handles grabbing the data regarding CCP's coronavirus confirmed cases and deaths from the website:
https://www.worldometers.info
"""
class DataGrabber:
    TARGET_DOMAIN = "https://www.worldometers.info/coronavirus"

    def grab_data(self, filename=''):
        cases = self.get_cases()
        deaths = self.get_deaths()

        if filename == '':
            filename = self.get_default_file_name()

        self.__save_data_to_file(filename, cases, deaths)

    def __get_table_content(self, path, table_selector, table_index):
        url = DataGrabber.TARGET_DOMAIN + "/" + path
        req = requests.get(url)
        content = req.content

        soup = BeautifulSoup(content, "html.parser")

        data = []
        table = soup.select(table_selector)[table_index].find("table")
        table_rows = table.select("tr")

        # The first row in the table is ignored (because it's the table's titles row), so we need to start from the second row.
        for i in range(1, len(table_rows)):
            current_value = int(table_rows[i].find_next("td").find_next("td").string.replace(",", ""))
            data.append(current_value)

        return data

    def get_cases(self):
        data = self.__get_table_content("coronavirus-cases", ".table-responsive", 2)

        return list(reversed(data))
    
    def get_deaths(self):
        data = self.__get_table_content("coronavirus-death-toll", ".table-responsive", 0)

        return list(reversed(data))

    def __save_data_to_file(self, filename, cases, deaths):
        data = []

        for i in range(0, len(cases)):
            data.append([i, cases[i], deaths[i]])
        
        with open("datasets/" + filename, 'w', newline='') as f:
            csv_writer = csv.writer(f, delimiter=',')
            csv_writer.writerows(data)

    def get_default_file_name(self):
        return "dataset_" + datetime.today().strftime('%Y-%m-%d') + ".csv"