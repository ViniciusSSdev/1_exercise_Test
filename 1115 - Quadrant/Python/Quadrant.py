class Quadrant:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def get_quadrant_coordinate(self):
        
        coordinateX = self.coordinates.coordinateX
        coordinateY = self.coordinates.coordinateY

        if (coordinateX > 0 and coordinateY > 0):
            return "First"
        elif (coordinateX < 0 and coordinateY > 0):
            return "Second"
        elif (coordinateX < 0 and coordinateY < 0):
            return "Third"
        elif (coordinateX > 0 and coordinateY < 0):
            return "Fourth"
        elif (coordinateX == 0 and coordinateY < 0 or coordinateY > 0):
            return "ordinate axis"
        elif (coordinateX > 0 or coordinateX < 0 and coordinateY == 0):
            return "abscissas axis"
        else:
            return ""
