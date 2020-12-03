# input must contain faces in this order: white, red, green, orange, blue, yellow


class Edge:

    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
        self.final_coordinates = self.get_final_coordinates()

    def get_final_coordinates(self):

        if self.name == 'RU' or self.name == 'UR':
            self.name = 'RU'
            a = (-1, 0, -1)
            return a

        if self.name == 'RG' or self.name == 'GR':
            self.name = 'RG'
            a = (1, 0, -1)
            return a

        if self.name == 'GO' or self.name == 'OG':
            self.name = 'GO'
            a = (1, 0, 1)
            return a

        if self.name == 'OU' or self.name == 'UO':
            self.name = 'OU'
            a = (-1, 0, 1)
            return a

        if self.name == 'RY' or self.name == 'YR':
            self.name = 'RY'
            a = (0, 1, -1)
            return a

        if self.name == 'GY' or self.name == 'YG':
            self.name = 'GY'
            a = (1, 1, 0)
            return a

        if self.name == 'OY' or self.name == 'YO':
            self.name = 'OY'
            a = (0, 1, 1)
            return a

        if self.name == 'UY' or self.name == 'YU':
            self.name = 'UY'
            a = (-1, 1, 0)
            return a

        if self.name == 'WR' or self.name == 'RW':
            self.name = 'WR'
            a = (0, -1, -1)
            return a

        if self.name == 'WG' or self.name == 'GW':
            self.name = 'WG'
            a = (1, -1, 0)
            return a

        if self.name == 'WO' or self.name == 'OW':
            self.name = 'WO'
            a = (0, -1, 1)
            return a

        if self.name == 'WU' or self.name == 'UW':
            self.name = 'WU'
            a = (-1, -1, 0)
            return a
