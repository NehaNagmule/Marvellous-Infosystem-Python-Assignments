import functools

checkEven = lambda no: (no % 2 == 0)
Square = lambda no: no * no
Add = lambda no1, no2: no1 + no2

def main():
    arr = list()

    print("Enter the size of list")
    size = int(input())

    for icnt in range(size):
        print("Enter element ", icnt + 1, " in list")
        arr.append(int(input()))

    print("List is ", arr)

    newdata = list(filter(checkEven, arr))
    print("After filter ", newdata)

    newdata1 = list(map(Square, newdata))
    print("After square ", newdata1)

    output = functools.reduce(Add, newdata1)
    print("Output is ", output)


if __name__ == "__main__":
    main()
