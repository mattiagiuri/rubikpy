# input must contain faces in this order: white, red, green, orange, blue, yellow


class Center:

    def __init__(self, name):
        self.name = name
        self.coordinates = self.get_coordinates()

    def get_coordinates(self):

        if self.name == 'W':
            a = (0, -1, 0)
            return a

        if self.name == 'R':
            a = (0, 0, -1)
            return a

        if self.name == 'G':
            a = (1, 0, 0)
            return a

        if self.name == 'O':
            a = (0, 0, 1)
            return a

        if self.name == 'B':
            a = (-1, 0, 0)
            return a

        if self.name == 'Y':
            a = (0, 1, 0)
            return a
