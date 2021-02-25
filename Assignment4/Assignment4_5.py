import MarvellousNum as mn
import functools

checkPrime = lambda no: (mn.checkPrime(no) == True)
Multipliedbytwo = lambda no: no * 2

max = 0
def Maximum(no1, no2):
    global max
    if(no1 > no2):
        if(no1 > max):
            max = no1
    elif (no2 > no1):
        if (no2 > max):
            max = no2

    return max

def main():
    arr = list()

    print("Enter the size of list")
    size = int(input())

    for icnt in range(size):
        print("Enter element ", icnt + 1, " in list")
        arr.append(int(input()))

    print("List is ", arr)

    newdata = list(filter(checkPrime, arr))
    print("After filter ", newdata)

    newdata1 = list(map(Multipliedbytwo, newdata))
    print("After multiplied by two ", newdata1)

    output = functools.reduce(Maximum, newdata1)
    print("Output is ", output)


if __name__ == "__main__":
    main()
