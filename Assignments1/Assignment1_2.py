def ChkNum(iNo):
    if iNo % 2 == 0:
        return True
    else:
        return False


def main():
    iNo = int(input("Enter number : "))
    bRet = ChkNum(iNo)
    if bRet == True:
        print("Even Number")
    else:
        print("Odd Number")


if __name__ == "__main__":
    main()
