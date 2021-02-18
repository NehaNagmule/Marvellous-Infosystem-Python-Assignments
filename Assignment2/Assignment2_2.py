def main():
    iNo = int(input("Enter number : "))
    for iCnt in range(iNo):
        for jCnt in range(iNo):
            print("* ", end='')
        print("\n", end='')     # or print() will work


if __name__ == "__main__":
    main()
