from enum import Enum
from math import *

# Не самый лучший способ множить конструторы
class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2

class Point:
    def __init__(self, x=0, y=0) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'{self.x=}, {self.y=}'

    class PointFactory:
        def new_cartesian_point(self, x, y):
            p = Point()
            p.x = x
            p.y = y
            return p
        
        def new_polar_point(self, rho, theta):
            return Point(rho * cos(theta), rho * sin(theta))
    
    factory = PointFactory()

if __name__ == "__main__":
    p1 = Point(2, 3)
    p2 = Point.factory.new_polar_point(1, 2)
    print(p1, p2)