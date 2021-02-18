def getSumOfDigits(iNo):
    if iNo == 0:
        return 0

    iSum = 0
    while iNo != 0:
        iDigit = int(iNo) % 10
        iNo = int(iNo) / 10
        if iNo != 0:
            iSum = iSum + int(iDigit)

    return iSum


def main():
    iNo = int(input("Enter number : "))
    print("The sum of digits in {} is {}".format(iNo, getSumOfDigits(iNo)))


if __name__ == "__main__":
    main()
