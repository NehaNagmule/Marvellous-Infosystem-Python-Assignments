import sys

def main():

    fname = sys.argv[1]

    fobj = open(fname,"r")  
        
    nfname = 'Demo.txt'
    
    newfobj = open(nfname,"w")
    newfobj.write(fobj.read())
        
    print("Copied successfully")
    
if __name__ == "__main__":
    main()