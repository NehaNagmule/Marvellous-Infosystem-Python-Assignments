import sys
import filecmp

def main():

    ffname = sys.argv[1]
    sfname = sys.argv[2]

    result = filecmp.cmp(ffname,sfname,shallow = False)     #shallow = true, it will only compare only file size, date modified etc
    
    if result == True:
        print("Files are identical")
    else:
        print("File are not identical")
    
if __name__ == "__main__":
    main()