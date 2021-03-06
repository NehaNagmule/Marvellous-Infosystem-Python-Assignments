class BookStore:
    noofbooks = 0

    def __init__(self, name, author):
        self.name = name
        self.author = author
        BookStore.noofbooks = BookStore.noofbooks + 1

    def Display(self):
        print("Name of the book ", self.name)
        print("Author of the book ", self.author)
        print("Number of the books ", BookStore.noofbooks)


def main():
    obj1 = BookStore("Linux System Programming", "Robert Love")
    obj1.Display()

    obj2 = BookStore("C Programming", "Dennis Ritchie")
    obj2.Display()

    print("Enter the name of the book")
    name = input()
    print("Enter the author of the book")
    author = input()

    obj3 = BookStore(name, author)
    obj3.Display()


if __name__ == "__main__":
    main()