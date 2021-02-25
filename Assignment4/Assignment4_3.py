import functools

checkNumber = lambda no: (no >= 70 and no <= 90)
Increment = lambda no: no + 10
Product = lambda no1, no2: no1 * no2

def main():
    arr = list()

    print("Enter the size of list")
    size = int(input())

    for icnt in range(size):
        print("Enter element ", icnt + 1, " in list")
        arr.append(int(input()))

    print("List is ", arr)

    newdata = list(filter(checkNumber, arr))
    print("After filter ", newdata)

    newdata1 = list(map(Increment, newdata))
    print("After increment ", newdata1)

    output = functools.reduce(Product, newdata1)
    print("Output is ", output)


if __name__ == "__main__":
    main()
