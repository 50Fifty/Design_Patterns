from design_patterns.creational.builder.builder import Builder
from design_patterns.creational.builder.director import Director

def test_1_builder_builds_diff_coffees():
    builder = Builder()
    director = Director()
    espresso = director.make_espresso(builder)
    assert espresso.name == 'Espresso'
    assert espresso.water == 50
    assert espresso.milk == 0
    assert espresso.coffee == 10
    assert espresso.sugar == 0
    assert espresso.cream == 0
    latte = director.make_latte(builder)
    assert latte.name == 'Latte'
    assert latte.water == 50
    assert latte.milk == 50
    assert latte.coffee == 10
    assert latte.sugar == 0
    assert latte.cream == 0
    cappuccino = director.make_cappuccino(builder)
    assert cappuccino.name == 'Cappuccino'
    assert cappuccino.water == 50
    assert cappuccino.milk == 50
    assert cappuccino.coffee == 10
    assert cappuccino.sugar == 10
    assert cappuccino.cream == 0