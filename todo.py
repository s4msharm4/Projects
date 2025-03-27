import argparse
import os
import json

JSON = "data.json"
CACHE_FILE = ".todo_cache"

def jsoncheck():
    if not os.path.exists(JSON):
        with open(JSON, "w") as f:
            json.dump({"name":None},f ,indent = 2)


def loadjson():
    with open(JSON,"r") as f:
        return json.load(f)

def savejson(data):
    with open(JSON,"w") as f:
        json.dump(data,f,indent = 2)

def set_name():
    name = input("Enter your name: ").strip()
    data = loadjson()
    data["name"] = name
    savejson(data)
    return name

def reset_name():
    """Deletes the stored name and asks for a new one."""
    data = loadjson()
    data["name"]=None
    savejson(data)
    print("Resseting done...")
    return set_name()



    

def main():
    parser = argparse.ArgumentParser(description="A simple todo list tool")
    parser.add_argument("--reset", action="store_true", help="Reset stored name")
    parser.add_argument("--exit", action="store_true", help="Exit the program")

    
    jsoncheck()
    data = loadjson()

    
    if not data["name"]:
        data["name"] = set_name()  # Ask for a name if it doesn't exist
    
    print(f"Hello, {data["name"]}!, what would you like to do today?") # greets only once until program is restarted
    
    while True:  # Keep running until --exit is passed
        command = input("What would you like to do?").strip()

        if command == "--exit":
            print("Goodbye!")
            break  

        args = parser.parse_args(command.split()) if command else argparse.Namespace(reset=False)

        if args.reset:
            name = reset_name()  # Reset and ask for a new name
        

        

if __name__ == "__main__":
    main()
