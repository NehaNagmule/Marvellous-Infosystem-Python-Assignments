isum = 0
def DigitCount(ino):
    global isum
    if ino != 0:
        iDigit = int(ino) % 10
        ino = int(ino) / 10
        isum = isum + iDigit
        DigitCount(ino)

    return isum

def main():
    print("Enter number ")
    value = int(input())
    iret = DigitCount(value)
    print("Addition is ", iret)


if __name__ == "__main__":
    main()