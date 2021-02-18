import Arithmetic


def main():
    iNo1 = int(input("Enter number 1 : "))
    iNo2 = int(input("Enter number 2 : "))

    print("Addition of {} and {} is {}".format(iNo1, iNo2, Arithmetic.Add(iNo1, iNo2)))
    print("Subtraction of {} and {} is {}".format(iNo1, iNo2, Arithmetic.Sub(iNo1, iNo2)))
    print("Multiplication of {} and {} is {}".format(iNo1, iNo2, Arithmetic.Mult(iNo1, iNo2)))
    print("Division of {} and {} is {}".format(iNo1, iNo2, Arithmetic.Div(iNo1, iNo2)))


if __name__ == "__main__":
    main()
