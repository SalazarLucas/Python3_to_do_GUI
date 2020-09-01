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
        """Returns a boolean. True if there are any stored tasks."""
        while True:
            try:
                with open('data_file.json', 'r') as file:
                    tasks = file.read()
                    file.close()
                break

            except FileNotFoundError:
                DataManager.create_data_file()

        if tasks:
            return True

        return False

    @classmethod
    def stored_tasks(cls):
        """Returns all tasks stored in data_file.json."""
        if DataManager.are_there_stored_tasks():
            with open('data_file.json', 'r') as file:
                tasks = json.load(file)
                file.close()
            return tasks

    @classmethod
    def update_data_file(cls, task_list):
        """Updates the data_file.json."""
        with open('data_file.json', 'w') as file:
            json.dump(task_list, file, indent=1)
            file.close()


DataManager.is_there_a_data_file()
