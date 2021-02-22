def Maximum(data):
    max = 0
    for i in range(len(data)):
        if data[i] > max:
            max = data[i]

    return max


def main():
    arr = list()

    print("Enter the size of list")
    size = int(input())

    for icnt in range(size):
        print("Enter element ", icnt + 1, " in list")
        arr.append(int(input()))

    print("List is ", arr)
    ret = Maximum(arr)
    print("Maximum of list is ", ret)


if __name__ == "__main__":
    main()
