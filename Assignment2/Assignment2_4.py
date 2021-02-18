def checkFactor(iValue, iNo):
    if iValue == 0 or iNo == 0:
        return False

    if iNo % iValue == 0:
        return True
    else:
        return False


def AddFactors(iNo):
    if iNo == 0:
        return 0

    iSum = 0
    for iCnt in range(iNo):
        if checkFactor(iCnt, iNo) == True:
            iSum = iSum + iCnt

    return iSum


def main():
    iNo = int(input("Enter number : "))
    print("Addition of factors of {} is {}".format(iNo, AddFactors(iNo)))


if __name__ == "__main__":
    main()
