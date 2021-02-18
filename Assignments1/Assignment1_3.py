def Add(iNo1, iNo2):
    return iNo1 + iNo2


def main():
    iNo1 = int(input("Enter number1 : "))
    iNo2 = int(input("Enter number2 : "))
    iRet = Add(iNo1, iNo2)
    print("Addition of {} and {} is {}".format(iNo1, iNo2, iRet))


if __name__ == "__main__":
    main()
