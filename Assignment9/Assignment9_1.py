import pathlib

def main():
    name = input("Enter the filename you want to check : ")
        
    file = pathlib.Path(name+".txt")
    if file.exists():
        print ("File exists")
    else:
        print ("File does not exist")


if __name__ == "__main__":
    main()