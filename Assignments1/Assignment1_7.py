def ChkNum(iNo):
    if iNo % 5 == 0:
        return True
    else:
        return False


def main():
    iNo = int(input("Enter number : "))
    bRet = ChkNum(iNo)
    if bRet == True:
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    main()
