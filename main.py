class Rectangle:
    def __init__(self , width, height):
        self.width = width
        self.height = height
    def perimeter(self):
        return (self.width + self.height)*2
    def area(self):
        return self.width * self.height
rezult = Rectangle(5 , 6)
print("Периметр:" , rezult.perimeter())
print("Площа:" , rezult.area())
