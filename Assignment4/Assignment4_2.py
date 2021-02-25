Multiplication = lambda no1, no2: no1 * no2

def main():

    print("Enter the number 1")
    no1 = (int(input()))
    print("Enter the number 2")
    no2 = (int(input()))

    print("Multiplication of {} and {} is {} ".format(no1, no2, Multiplication(no1, no2)))


if __name__ == "__main__":
    main()
