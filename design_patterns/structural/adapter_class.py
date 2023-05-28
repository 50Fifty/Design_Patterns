class RoundPeg:
    def __init__(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

class RoundHole: # Existing Class
    def __init__(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius
    
    def fits(self, peg: RoundPeg) -> bool:
        return True if peg.getRadius() <= self.getRadius() else False

class SquarePeg: # New Service
    def __init__(self, width):
        self.__width = width

    def getWidth(self):
        return self.__width
    
class SquarePegAdapter(SquarePeg, RoundHole):
    def __init__(self, width):
        SquarePegAdapter.__init__(self, width=width)
    
    def getRadius(self):
        from math import sqrt
        return self.getWidth() * sqrt(2) / 2
    
if __name__ == "__main__":
    round_peg = RoundPeg(5)
    round_hole = RoundHole(5)

    # square_peg = SquarePeg(5)
    square_peg_adapter = SquarePegAdapter(5)
    square_peg_adapter.getRadius()
    square_peg_adapter.getWidth()
