# input must contain faces in this order: white, red, green, orange, blue, yellow


class Vertex:

    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates
        self.final_coordinates = self.get_final_coordinates()

    def get_final_coordinates(self):

        if self.name == 'WUR' or self.name == 'WRU' or self.name == 'RUW' or self.name == 'RWU' or self.name == 'UWR' or self.name == 'URW':
            self.name = 'WRU'
            a = (-1, -1, -1)
            return a

        if self.name == 'WRG' or self.name == 'WGR' or self.name == 'RGW' or self.name == 'RWG' or self.name == 'GWR' or self.name == 'GRW':
            self.name = 'WRG'
            a = (1, -1, -1)
            return a

        if self.name == 'WGO' or self.name == 'WOG' or self.name == 'GWO' or self.name == 'GOW' or self.name == 'OGW' or self.name == 'OWG':
            self.name = 'WGO'
            a = (1, -1, 1)
            return a

        if self.name == 'WOU' or self.name == 'WUO' or self.name == 'OUW' or self.name == 'OWU' or self.name == 'UWO' or self.name == 'UOW':
            self.name = 'WOU'
            a = (-1, -1, 1)
            return a

        if self.name == 'YUR' or self.name == 'YRU' or self.name == 'RUY' or self.name == 'RYU' or self.name == 'UYR' or self.name == 'URY':
            self.name = 'RUY'
            a = (-1, 1, -1)
            return a

        if self.name == 'YRG' or self.name == 'YGR' or self.name == 'RGY' or self.name == 'RYG' or self.name == 'GYR' or self.name == 'GRY':
            self.name = 'RGY'
            a = (1, 1, -1)
            return a

        if self.name == 'YGO' or self.name == 'YOG' or self.name == 'GYO' or self.name == 'GOY' or self.name == 'OGY' or self.name == 'OYG':
            self.name = 'GOY'
            a = (1, 1, 1)
            return a

        if self.name == 'YOU' or self.name == 'YUO' or self.name == 'OUY' or self.name == 'OYU' or self.name == 'UYO' or self.name == 'UOY':
            self.name = 'OUY'
            a = (-1, 1, 1)
            return a
