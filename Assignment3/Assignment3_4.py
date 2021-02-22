def Frequency(data, value):
    ifcnt = 0
    for i in range(len(data)):
        if data[i] == value:
            ifcnt = ifcnt + 1

    return ifcnt


def main():
    arr = list()

    print("Enter the size of list")
    size = int(input())

    for icnt in range(size):
        print("Enter element ", icnt + 1, " in list")
        arr.append(int(input()))

    print("List is ", arr)

    print("Enter the number you want to check the frequency of")
    value = int(input())
    ret = Frequency(arr, value)
    print("Frequency of {} in list is {}".format(value, ret))


if __name__ == "__main__":
    main()
