from data_grabbers.data_grabber import DataGrabber
from data_grabbers.graphs_data_grabber import GraphsDataGrabber

class DeathsDataGrabber(DataGrabber):
    DATASET_PREFIX = "deaths"
    PATH = "worldwide-graphs"
    GRAPH_ID = "coronavirus-deaths-linear"
    SERIES_NAME = "Deaths"

    def __init__(self):
        super()

    def grab_data(self):
        graphs_grabber = GraphsDataGrabber()

        data = graphs_grabber.get_data(path=DeathsDataGrabber.PATH, graph_id=DeathsDataGrabber.GRAPH_ID, series_name=DeathsDataGrabber.SERIES_NAME)
        filename = self.get_dataset_file_name()

        self.save_data_to_file(filename, data)

    def get_dataset_file_name(self, dataset_date=""):
        return super().get_dataset_file_name(DeathsDataGrabber.DATASET_PREFIX, dataset_date=dataset_date)
