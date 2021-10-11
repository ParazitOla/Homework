#### Task 6.2 Implement custom dictionary that will memorize 10 latest changed keys.
# Using method "get_history" return this keys.

class HistoryDict:
    total_list = []

    def __init__(self, *args):
        self.total_list = list(args[0].keys())

    def set_value(self, *args):
        lst = list(args[0].keys())
        self.total_list.extend(lst)
        if len(self.total_list) > 10:
            self.total_list.pop(0)

    def get_history(self):
        return print(self.total_list)


d = HistoryDict({"foo": 42})
d.set_value({"doo1": 1})
d.set_value({"foo2": 2})
d.set_value({"doo": 3})
d.set_value({"foo": 4})
d.set_value({"doo": 5})
d.set_value({"foo": 6})
d.set_value({"doo": 7})
d.set_value({"foo": 8})
d.set_value({"doo9": 9})
d.set_value({"foo10": 10})
d.set_value({"doo11": 11})
d.set_value({"foo12": 12})

d.get_history()
