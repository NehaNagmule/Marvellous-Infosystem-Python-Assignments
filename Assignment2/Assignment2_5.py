def checkFactor(iValue, iNo):
    if iValue == 0 or iNo == 0:
        return False

    if iNo % iValue == 0:
        return True
    else:
        return False


def checkPrime(iNo):
    if iNo == 0 or iNo == 1:
        return False

    iCnt = 2
    while iCnt <= iNo:
        if checkFactor(iCnt, iNo) == True:
            break
        iCnt = iCnt + 1

    if iCnt == iNo:
        return True
    else:
        return False


def main():
    iNo = int(input("Enter number : "))
    bret = checkPrime(iNo)
    if bret == True:
        print("The number {} is Prime Number".format(iNo))
    else:
        print("The number {} is Not Prime Number".format(iNo))


if __name__ == "__main__":
    main()
