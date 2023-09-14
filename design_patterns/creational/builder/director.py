class Director:
    def __init__(self):
        pass

    def make_espresso(self, builder):
        builder.reset()
        builder.set_name('Espresso')
        builder.set_water(50)
        builder.set_milk(0)
        builder.set_coffee(10)
        builder.set_sugar(0)
        builder.set_cream(0)
        return builder.make()

    def make_latte(self, builder):
        builder.reset()
        builder.set_name('Latte')
        builder.set_water(50)
        builder.set_milk(50)
        builder.set_coffee(10)
        builder.set_sugar(0)
        builder.set_cream(0)
        return builder.make()
    
    def make_cappuccino(self, builder):
        builder.reset()
        builder.set_name('Cappuccino')
        builder.set_water(50)
        builder.set_milk(50)
        builder.set_coffee(10)
        builder.set_sugar(10)
        builder.set_cream(0)
        return builder.make()