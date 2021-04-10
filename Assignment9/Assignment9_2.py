
def main():
    fname = input("Enter the filename that you want to read ")
    
    print("Your contents are : ")
    fobj = open(fname,"r")
    print(fobj.read())
    
if __name__ == "__main__":
    main()