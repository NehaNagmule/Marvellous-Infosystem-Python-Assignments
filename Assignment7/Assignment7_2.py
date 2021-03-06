class BankAccount:
    ROI = 10.5

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def Display(self):
        print("Name of the account holder ", self.name)
        print("Amount is ", self.amount)

    def Deposit(self, amount):
        self.amount = self.amount + amount

    def Withdraw(self, amount):
        if self.amount > 0:
            self.amount = self.amount - amount
        else:
            print("Your balance is nil. Transaction aborted")

    def CalculateInterest(self, time):
        if self.amount > 0:
            return ( ( self.amount * BankAccount.ROI * time ) / 100 )
        else:
            print("Your balance is nil. Transaction aborted")
            return 0


def main():

    print("Enter name of the account holder")
    name = input()
    print("Enter the amount")
    amount = float(input())
    obj1 = BankAccount(name, amount)
    obj1.Display()

    print("Enter the amount to deposit")
    deposit = float(input())
    obj1.Deposit(deposit)
    obj1.Display()

    print("Enter the amount to withdraw")
    withdraw = float(input())
    obj1.Withdraw(withdraw)
    obj1.Display()

    print("Enter the time period to get the interest")
    time = float(input())
    ret = obj1.CalculateInterest(time)
    if ret > 0:
        print("Interest received for {} is {}". format(time, ret))


if __name__ == "__main__":
    main()