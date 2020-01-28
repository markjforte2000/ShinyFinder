

class MenuItem(object):

    def __init__(self, name, selected, position):
        self.__name = name
        self.__selected = selected
        self.__position = position

    @property
    def name(self):
        return self.__name

    @property
    def is_selected(self):
        return self.__selected

    @property
    def position(self):
        return self.__position

