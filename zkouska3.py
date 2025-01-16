# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte dvě podtřídy třídy `Shape`: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`, která spočítá plochu obdelníku (zaokrouhlenou na 1 desetinné místo).
# - `Circle` má atribut `radius` a implementuje metodu `area`, která spočítá plochu kruhu (zaokrouhlenou na 1 desetinné místo).
# - ve třídě `Circle` navíc implementujte metodu `__str__`, která vrátí řetězec ve tvaru `{self.shape_name} with a radius of {self.radius} has an area of {self.area}`.


import math # import knihovny math pro pouziti pi

class Shape():

    def __init__(self, shape_name=None):
        self.shape_name = shape_name
    
    def __str__(self): 
        return f'{self.shape_name} shape with area {self.area()}'

    def area(self):
        return 0.0


# ZDE NAPIŠTE VÁŠ KÓD
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(shape_name="Rectangle") #jmeno nasi zakladni tridy
        self.width = width
        self.height = height
    
    def area(self):
        vysledek = self.width * self.height #vypočítá šírku * výšku obdelníku 
        return round(vysledek, 1) #funkce round na zaokrouhleni
    

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(shape_name="Circle") #jmeno nasi zakladni tridy
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius ** 2, 1) #vypocet plochy kruhu, zaokrouhleni na 1 desetinné číslo
    

    def __str__(self): #specialni dunder/magic metoda pro objektů jako řetězec
        return f"{self.shape_name} with a radius of {self.radius} has an area of {self.area()}" 

from unittest.mock import patch, MagicMock, mock_open


# Unit testy
def test_shapes():
    rect = Rectangle(4, 5)
    assert rect.area() == 20.0
    assert str(rect) == "Rectangle shape with area 20.0"

    circle = Circle(3)
    assert round(circle.area(), 1) == 28.3
    assert str(circle) == "Circle shape with a radius of 3 has an area of 28.3"


if __name__ == "__main__":
    shape = Shape()
    print(shape)
    rect = Rectangle(4, 5)
    print(rect)
    circle = Circle(3)
    print(circle)