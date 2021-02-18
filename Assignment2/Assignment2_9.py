def getNumberOfDigits(iNo):
    if iNo == 0:
        return 0

    iDigitCount = 0
    while iNo != 0:
        iNo = int(iNo) / 10
        if iNo != 0:
            iDigitCount = iDigitCount + 1

    return iDigitCount


def main():
    iNo = int(input("Enter number : "))
    print("The number of digits in {} is {}".format(iNo, getNumberOfDigits(iNo)))


if __name__ == "__main__":
    main()
