class Arithmetic:

    def __init__(self, value):
        self.value = value
        self.arr = []

    def ChkPrime(self):
        if self.value == 0 or self.value == 1:
            return False
        else:
            icnt = 2
            while icnt <= self.value:
                if self.value % icnt == 0:
                    break
                icnt = icnt + 1

            if icnt == self.value:
                return True
            else:
                return False

    def ChkPerfect(self):
        sum = 0
        if self.value == 0:
            return False
        else:
            for i in range(1, self.value):
                if self.value % i == 0:
                    sum = sum + i

            if sum == self.value:
                return True
            else:
                return False

    def Factors(self):
        if self.value == 0:
            print("Not possible")
        else:
            for i in range(1, self.value):
                if self.value % i == 0:
                    self.arr.append(i)

            print("Factors are : ", self.arr)

    def SumFactors(self):
        sum = 0
        for i in range(len(self.arr)):
            sum = sum + self.arr[i]

        return sum


def main():

    print("Enter the number")
    value = int(input())


    obj1 = Arithmetic(value)
    ret = obj1.ChkPrime()
    if ret == True:
        print("The number is prime")
    else:
        print("The number is not prime")

    obj1.Factors()
    ret = obj1.SumFactors()
    print("Sum of factors are ", ret)

    ret = obj1.ChkPerfect()
    if ret == True:
        print("The number is Perfect")
    else:
        print("The number is not Perfect")


if __name__ == "__main__":
    main()