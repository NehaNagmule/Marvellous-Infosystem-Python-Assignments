def ChkNum(iNo):
    if iNo > 0:
        return True
    elif iNo < 0:
        return False
    else:
        return 0

def main():
    iNo = int(input("Enter number : "))
    bRet = ChkNum(iNo)
    if bRet == True:
        print("Positive Number")
    elif bRet == False and bRet is False:
        print("Negative Number")
    else:
        print("Zero")


if __name__ == "__main__":
    main()
