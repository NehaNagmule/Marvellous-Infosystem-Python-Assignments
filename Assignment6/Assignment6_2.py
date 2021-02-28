class Circle:
    PI = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def Accept(self, radius):
        self.radius = radius

    def CalculateArea(self):
        self.area = Circle.PI * self.radius * self.radius

    def CalculateCircumference(self):
        self.circumference = 2 * Circle.PI * self.radius

    def Display(self):
        print("Radius of circle is ", self.radius)
        print("Area of circle is ", self.area)
        print("Circumference of circle is ", self.circumference)


def main():

    print("Enter the radius of first circle")
    radius = int(input())

    obj1 = Circle()
    obj1.Accept(radius)
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    print()
    print("Enter the radius of second circle")
    radius = int(input())

    obj2 = Circle()
    obj2.Accept(radius)
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()


if __name__ == "__main__":
    main()