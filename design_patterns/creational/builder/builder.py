from design_patterns.creational.builder.coffee import Coffee

class Builder:
    def __init__(self) -> None:
        self.coffee = None

    def reset(self):
        self.coffee = Coffee()

    def set_name(self, name):
        self.coffee.name = name

    def set_water(self, water):
        self.coffee.water = water

    def set_milk(self, milk):
        self.coffee.milk = milk

    def set_coffee(self, coffee):
        self.coffee.coffee = coffee
    
    def set_sugar(self, sugar):
        self.coffee.sugar = sugar

    def set_cream(self, cream):
        self.coffee.cream = cream

    def get_coffee(self):
        return self.coffee
    
    def make(self):
        return self.coffee