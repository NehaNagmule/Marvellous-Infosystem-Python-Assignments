def Minimum(data):
    min = data[len(data)-1]

    for i in range(len(data)):
        if data[i] < min:
            min = data[i]

    return min


def main():
    arr = list()

    print("Enter the size of list")
    size = int(input())

    for icnt in range(size):
        print("Enter element ", icnt + 1, " in list")
        arr.append(int(input()))

    print("List is ", arr)
    ret = Minimum(arr)
    print("Minimum of list is ", ret)


if __name__ == "__main__":
    main()
