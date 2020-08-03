import json


class ToDoData(object):
    try:
        with open('lists.json', 'r') as file:
            lists = json.load(file)
        file.close()

    except FileNotFoundError:
        with open('lists.json', 'w') as file:
            lists = {'All Lists': {},
                     'Default': {},
                     'Personal': {},
                     'Shopping': {},
                     'Wishlist': {},
                     'Work': {},
                     'Finished': {},
                     'New List': {}}
            json.dump(lists, file, indent=1)
        file.close()

    @classmethod
    def set_lists(cls, obj):
        with open('lists.json', 'w') as file:
            json.dump(obj, file, indent=1)
        file.close()
