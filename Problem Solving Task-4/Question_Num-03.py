
#Q3 From the given List create two class Methods Area and Perimeter which will be going to calculate the Area and Perimeter

class Circle:
    def __init__(self, r):
        self.radius = r
    def area(self):
        return 3.141 * (self.radius ** 2)
    def perimeter(self):
        return 2 * 3.141 * self.radius
NewCircle = Circle(5)
print(NewCircle.area())
print(NewCircle.perimeter())
