class Parallelogram:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def get_area(self):
        area = self.width * self.length
        return area
a = Parallelogram(45, 50)
print(a.get_area())
class Square(Parallelogram):
    def __init__(self, width):
        self.width = width
    def get_area(self):
        area = self.width ** 2
        return area
b = Square(50)
print(b.get_area())
    

    