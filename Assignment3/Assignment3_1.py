def Addition(data):
    sum = 0
    for i in range(len(data)):
        sum = sum + data[i]

    return sum


def main():
    arr = list()

    print("Enter the size of list")
    size = int(input())

    for icnt in range(size):
        print("Enter element ", icnt + 1, " in list")
        arr.append(int(input()))

    print("List is ", arr)
    ret = Addition(arr)
    print("Addition of list is ", ret)


if __name__ == "__main__":
    main()
