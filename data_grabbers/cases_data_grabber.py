from data_grabbers.data_grabber import DataGrabber

class CasesDataGrabber(DataGrabber):
    DATASET_PREFIX = "cases"

    def __init__(self):
        super()

    def grab_data(self):
        data = self.__get_cases()
        filename = self.get_dataset_file_name()

        self.save_data_to_file(filename, data)

    def __get_cases(self):
        data = self.get_table_content("coronavirus-cases", ".table-responsive", 2)

        return list(reversed(data))

    def get_dataset_file_name(self, dataset_date=""):
        return super().get_dataset_file_name(CasesDataGrabber.DATASET_PREFIX, dataset_date=dataset_date)
