class Demo:
    value = 101

    def __init__(self, i, j):
        self.no1 = i
        self.no2 = j

    def Fun(self):
        print(self.no1)
        print(self.no2)

    def Gun(self):
        print(self.no1)
        print(self.no2)


def main():

    print("Enter the number 1")
    value1 = int(input())

    print("Enter the number 2")
    value2 = int(input())

    obj1 = Demo(value1, value2)
    obj2 = Demo(value1, value2)

    obj1.Fun()
    obj1.Gun()
    obj2.Fun()
    obj2.Gun()


if __name__ == "__main__":
    main()