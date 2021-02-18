def ChkEven(iNo):
    if iNo % 2 == 0:
        return True

def main():
    iNo = int(input("Enter number : "))
    iCheckCount = 0
    iCnt = 1
    while iCheckCount < 10:
        if ChkEven(iCnt) == True:
            print(iCnt, " ", end='')
            iCheckCount = iCheckCount + 1

        if iCheckCount == iNo:
            break

        iCnt = iCnt + 1


if __name__ == "__main__":
    main()
