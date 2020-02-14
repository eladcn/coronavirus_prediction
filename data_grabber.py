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

    def grab_data(self):
        cases = self.get_cases()
        deaths = self.get_deaths()
        cases_filename = self.get_dataset_file_name("cases")
        deaths_filename = self.get_dataset_file_name("deaths")

        self.__save_data_to_file(cases_filename, cases)
        self.__save_data_to_file(deaths_filename, deaths)

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

    def __save_data_to_file(self, filename, data):
        data_to_save = []

        # There are more 
        for i in range(0, len(data)):
            data_to_save.append([i, data[i]])
        
        with open("datasets/" + filename, 'w', newline='') as f:
            csv_writer = csv.writer(f, delimiter=',')
            csv_writer.writerows(data_to_save)

    def get_dataset_file_name(self, dataset_type, dataset_date=""):
        filename = dataset_type + "_dataset_"

        if dataset_date == "":
            filename += datetime.today().strftime('%Y-%m-%d')
        else:
            filename += dataset_date
        
        filename += ".csv"
        
        return filename
