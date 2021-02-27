ifact = 1
def getFact(ino):
    global ifact
    if ino != 0:
        ifact = ifact * ino
        ino = ino - 1
        getFact(ino)

    return ifact

def main():
    print("Enter number ")
    value = int(input())
    iret = getFact(value)
    print("Factorial is ", iret)


if __name__ == "__main__":
    main()