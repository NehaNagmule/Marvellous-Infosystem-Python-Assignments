icnt = 1
def DisplayPattern(ino):
    global icnt
    if ino != 0:
        print(icnt, " ", end='')
        icnt =icnt + 1
        ino = ino - 1
        DisplayPattern(ino)


def main():
    print("Enter number ")
    value = int(input())
    DisplayPattern(value)


if __name__ == "__main__":
    main()