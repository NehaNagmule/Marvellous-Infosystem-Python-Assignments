import sys
import filecmp

def main():

    fname = sys.argv[1]
    search = sys.argv[2]
    count = 0

    fobj = open(fname, 'r')
    data = fobj.read()
    count = data.count(search)
            
    print("Count is ", count)
    
if __name__ == "__main__":
    main()