from builder import Builder
from director import Director

def main():
    builder = Builder()
    director = Director()
    espresso = director.make_espresso(builder)
    print(espresso)
    latte = director.make_latte(builder)
    print(latte)
    cappuccino = director.make_cappuccino(builder)
    print(cappuccino)

if __name__ == '__main__':
    main()