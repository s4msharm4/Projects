import argparse
import os

cache = ".catch"

def getname():
    if os.path.exists(cache):
        with open(cache,"r") as f:
            return f.read().strip()
    return None
       
def setname():
    name = input("Enter name: ").strip()
    with open(cache,"w") as f:
        f.write(name)
    return name   
def resetname():
    if os.path.exists(cache):
        os.remove(cache)
        print("Name reset successful") 
    else:
        print("there is no one")
    return setname() 


def main():
    parser = argparse.ArgumentParser(description = "A simple todo list tool")
    parser.add_argument("--reset",action="store_true",help="Reset the name")
    args = parser.parse_args()


    if args.reset:
        name = resetname()
    else:
        name = getname()
        
    print(f"Hello {name}")    


    

if __name__=="__main__":
    main()