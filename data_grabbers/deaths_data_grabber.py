from data_grabbers.data_grabber import DataGrabber

class DeathsDataGrabber(DataGrabber):
    DATASET_PREFIX = "deaths"

    def __init__(self):
        super()

    def grab_data(self):
        data = self.__get_deaths()
        filename = self.get_dataset_file_name()

        self.save_data_to_file(filename, data)

    def __get_deaths(self):
        data = self.get_table_content("coronavirus-death-toll", ".table-responsive", 0)

        return list(reversed(data))

    def get_dataset_file_name(self, dataset_date=""):
        return super().get_dataset_file_name(DeathsDataGrabber.DATASET_PREFIX, dataset_date=dataset_date)
