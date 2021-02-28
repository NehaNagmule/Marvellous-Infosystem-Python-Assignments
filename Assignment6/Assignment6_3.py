class Arithmetic:

    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def Addition(self):
        return self.value1 + self.value2

    def Subtraction(self):
        return self.value1 - self.value2

    def Multiplication(self):
        return self.value1 * self.value2

    def Division(self):
        if self.value2 == 0:
            return "Not possible"
        else:
            return self.value1 / self.value2


def main():

    print("Enter the value 1")
    value1 = int(input())

    print("Enter the value 2")
    value2 = int(input())

    obj1 = Arithmetic()
    obj1.Accept(value1, value2)
    ret = obj1.Addition()
    print("Addition is ", ret)
    ret = obj1.Subtraction()
    print("Subtraction is ", ret)
    ret = obj1.Multiplication()
    print("Multiplication is ", ret)
    ret = obj1.Division()
    print("Division is ", ret)

    print()
    print("Enter the value 1")
    value1 = int(input())

    print("Enter the value 2")
    value2 = int(input())

    obj2 = Arithmetic()
    obj2.Accept(value1, value2)
    ret = obj2.Addition()
    print("Addition is ", ret)
    ret = obj2.Subtraction()
    print("Subtraction is ", ret)
    ret = obj2.Multiplication()
    print("Multiplication is ", ret)
    ret = obj2.Division()
    print("Division is ", ret)


if __name__ == "__main__":
    main()