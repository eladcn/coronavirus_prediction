import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv
import json
import re
import ast

""" 
This class handles grabbing the data regarding CCP's coronavirus confirmed cases and deaths from the website:
https://www.worldometers.info
"""
class GraphsDataGrabber:
    TARGET_DOMAIN = "https://www.worldometers.info/coronavirus/"

    def get_data(self, path, graph_id, series_name):
        url = GraphsDataGrabber.TARGET_DOMAIN + path
        req = requests.get(url, timeout=20)
        content = req.content.decode("utf-8")

        data_regex = r"(Highcharts\.chart\('" + graph_id + r"'[\s\S]*?series:\s*\[\{[\s\S]*?name:\s*?'" + series_name + r"'[\s\S]*?data:\s*?)(\[(null|[0-9,-])*?\])"
        data_matches = re.finditer(data_regex, content)

        for match in data_matches:
            match_data = match.group(2).replace("null", "0")
            return ast.literal_eval(match_data)

        return []
