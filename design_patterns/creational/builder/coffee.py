class Coffee:
    def __init__(self) -> None:
        self.name = None
        self.water = None
        self.milk = None
        self.coffee = None
        self.sugar = None
        self.cream = None

    def __str__(self) -> str:
        return f'{self.name}\n==========\nWater: {self.water}\nMilk: {self.milk}\nCoffee: {self.coffee}\nSugar: {self.sugar}\nCream: {self.cream}\n'