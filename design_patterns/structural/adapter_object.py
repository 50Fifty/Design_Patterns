"""
Adapter: Object version. (Applicable to most if not all programming languages)

This is an example of the Adapter design pattern implemented in Python.
The Adapter pattern is used to convert the interface of a class into another interface clients expect.
Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.
The Adapter pattern is also referred to as the Wrapper Pattern.

In this example we have a RoundHole class that is compatible with RoundPegs.
But there are SquarePegs that we want to fit into the RoundHole.
To make the SquarePegs compatible with the RoundHole we create a SquarePegAdapter class.

Idea from: https://refactoring.guru/design-patterns/adapter
"""

class RoundPeg:
    """
    RoundPegs are compatible with RoundHoles.
    """

    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

class RoundHole: 
    """
    RoundHoles are compatible with RoundPegs.
    """

    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius
    
    def fits(self, peg: RoundPeg) -> bool:
        if not isinstance(peg, RoundPeg):
            raise TypeError('peg must be of type RoundPeg')
        
        return peg.get_radius() <= self.get_radius()

class SquarePeg:
    """
    SquarePegs are not compatible with RoundHoles (e.g. they are a new class/implementation).
    """

    def __init__(self, width):
        self.__width = width

    def get_width(self):
        return self.__width
    
class SquarePegAdapter(RoundPeg):
    """
    SquarePegAdapter is a subclass of RoundPeg.
    SquarePegAdapter makes use of inheritance to inherit from RoundPeg.
        - This allows SquarePegAdapter to be used as a RoundPeg.
    SquarePegAdapter also makes use of composition to store a SquarePeg object.
        - This allows SquarePegAdapter to be used as a SquarePeg.
    """

    def __init__(self, peg:SquarePeg):
        from math import sqrt
        self.__square_peg = peg
        super().__init__(self.__square_peg.get_width() * sqrt(2) / 2)