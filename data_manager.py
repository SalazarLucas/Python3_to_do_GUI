import jsonpickle
import json


class DataManager(object):
    @classmethod
    def is_there_a_data_file(cls):
        """This method verifies if there is a json file named data_file.json, if not,
        it creates it calling create_data_file() method."""
        try:
            with open('data_file.json', 'r') as file:
                file.close()

        except FileNotFoundError:
            DataManager.create_data_file()

    @classmethod
    def create_data_file(cls):
        """This method creates a data file if it doesn't exist."""
        with open('data_file.json', 'w') as file:
            file.close()

    @classmethod
    def are_there_stored_tasks(cls):
        pass

    @classmethod
    def stored_tasks(cls):
        pass

    @classmethod
    def update_data_file(cls):
        pass


DataManager.is_there_a_data_file()
