# Принцип открытости закрытости - добавляем новый функционал через расширение, а не модифицикацию.
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

# При необходимости фильтрации создаем класс и добаляем методы до бесконечности, что плохо
class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p
    
    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p

# Реализуем именно отдельные классы для расширения функционала.
class Specification:
    def is_satisfied(self, item):
        pass

class Filter:
    def filter(self, items, spec):
        pass

class ColorSpecification(Specification):
    def __init__(self, color) -> None:
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size) -> None:
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item
# Для комбинации спецификаций
class AndSpecifications(Specification):
    def __init__(self, *args) -> None:
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))

if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    pf = ProductFilter()
    print('Green products (old):')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f' - {p.name} is green')

    bf = BetterFilter()
    print('Green products (new):')
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f' - {p.name} is green')
    
    print('Large products:')
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f' - {p.name} is large')
    
    print('Large blue items:')
    large_blue = AndSpecifications(large,
        ColorSpecification(Color.BLUE)
        )
    for p in bf.filter(products, large_blue):
        print(f' - {p.name} is large and blue')
