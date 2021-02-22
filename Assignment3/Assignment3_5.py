import MarvellousNum as mn

def ListPrime(data):
    brr = list()
    icnt = 0
    for icnt in range(len(data)):
        if mn.checkPrime(data[icnt]):
            brr.append(int(data[icnt]))

    print("Prime number list ", brr)

    ret = mn.Addition(brr)

    return ret

def main():
    arr = list()

    print("Enter the size of list")
    size = int(input())

    for icnt in range(size):
        print("Enter element ", icnt + 1, " in list")
        arr.append(int(input()))

    print("List is ", arr)

    ret = ListPrime(arr)
    print("Addition is ",ret)


if __name__ == "__main__":
    main()
