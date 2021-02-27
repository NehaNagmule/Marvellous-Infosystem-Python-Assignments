def DisplayPattern(ino):
    if ino != 0:
        ino = ino - 1
        print("* ", end='')
        DisplayPattern(ino)


def main():
    print("Enter number ")
    value = int(input())
    DisplayPattern(value)


if __name__ == "__main__":
    main()