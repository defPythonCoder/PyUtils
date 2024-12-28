from os import name, system
import os
import sys

if len(sys.argv) > 1:
    working_dir = sys.argv[1]
    os.chdir(working_dir)

RESET = "\033[0m"
BOLD = "\033[1m"
BRIGHT = "\033[97m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BLUE = "\033[94m"

repeat = ["dict", "list"]

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

typeddicts = {}
def getTypes(name, data):
    global typeddicts
    typeddicts[name] = {}
    if type(data).__name__ == "dict":
        for i in data:
            t = type(data[i]).__name__
            if t in repeat:
                if t == "dict":
                    getTypes(f"{i}{t}", data[i])
                    typeddicts[name][i] = f"{i}{t}"
                elif t == "list":
                    Lelements = []
                    for _ in data[i]:
                        if type(_).__name__ == "dict":
                            getTypes(f"{i}dict", _)
                            Lelements.append(f"{i}dict")
                        else:
                            Lelements.append(type(_).__name__)
                    if len(set(Lelements)) == 1:
                        typeddicts[name][i] = f"List[{Lelements[0]}] # contains {len(Lelements)} elements"
                    else:
                        typeddicts[name][i] = f"List[{', '.join(Lelements)}]"
            else:
                typeddicts[name][i] = t
    elif type(data).__name__ == "list":
        list_items = []
        pass


def main(data):
    global typeddicts
    getTypes("main", data)
    rev_dict = dict(reversed(list(typeddicts.items())))
    print(GREEN + BOLD + "Processed Output: " + RESET + YELLOW)
    for item in rev_dict:
        print(f"\nclass {item}(TypedDict):")
        for value in rev_dict[item]:
            print(f"    {value}: {rev_dict[item][value]}")
    print(RESET)


def read_data_from_file(file_path):
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            if file_path.endswith('.json') or file_path.endswith('.txt'):
                return file.read()
            else:
                print(RED + BOLD + "Unsupported file format. Use .json or .txt." + RESET)
                return None
    except Exception as e:
        print(RED + BOLD + f"Error reading file: {e}" + RESET)
        return None

def get_input_type():
    print(CYAN + BOLD + "Choose input type:" + RESET)
    print(YELLOW + BOLD + "1. Dictionary" + RESET)
    print(YELLOW + BOLD + "2. Json" + RESET)
    
    choice = input(CYAN + BOLD + "Enter your choice (1/2): " + RESET)
    return choice
def get_input_choice(data_type):
    print(CYAN + BOLD + f"Choose {BLUE}{data_type}{CYAN} input method:" + RESET)
    print(YELLOW + BOLD + "1. Input directly" + RESET)
    print(YELLOW + BOLD + "2. Load from .txt file" + RESET)
    print(YELLOW + BOLD + "3. Load from .json file" + RESET)
    
    choice = input(CYAN + BOLD + "Enter your choice (1/2/3): " + RESET)
    return choice

def handle_user_input():
    data_type = None
    data_format = None

    datatype = get_input_type()
    if datatype == '1':
        data_type = "dict"
    elif datatype == '2':
        data_type = "json"
    else:
        print(RED + BOLD + "Invalid choice." + RESET)
        return None

    clear()
    choice = get_input_choice(data_type)
    if choice == '1':
        data_format = "input"
    elif choice == '2':
        data_format = "txt"
    elif choice == '3':
        data_format = "json"
    else:
        print(RED + BOLD + "Invalid choice." + RESET)
        return None

    return data_type, data_format

def get_data(data_type, data_format):
    if data_format == "input":
        try:
            data = input(GREEN + BOLD + f"Enter your {BLUE}{data_type}{GREEN}: " + RESET)
        except Exception as e:
            print(RED + BOLD + f"Error reading input: {e}" + RESET)
            return None
    elif data_format in ['txt', 'json']:
        file_path = input(GREEN + BOLD + f"Enter the path to your {BLUE}.{data_format}{GREEN} file containing {BLUE}{data_type}{GREEN}: " + RESET)
        data = read_data_from_file(file_path)
    else:
        print(RED + BOLD + "Invalid choice." + RESET)
        return None
    
    if data is not None:
        if data_type == "json":
            import json
            try:
                loaded_data = json.loads(data)
            except Exception as e:
                print(RED + BOLD + f"Error parsing json: {e}" + RESET)
                return None
        else:
            try:
                loaded_data = eval(data)
            except Exception as e:
                print(RED + BOLD + f"Error parsing dictionary: {e}" + RESET)
                return None
        return loaded_data
    else:
        print(RED + BOLD + "No valid data provided. Exiting." + RESET)
        return None


if __name__ == "__main__":
    print(BLUE + BOLD + BRIGHT + "Welcome to the Dictionary Processor!" + RESET)
    datatype, dataformat = handle_user_input()
    if datatype is not None:
        clear()
        data = get_data(datatype, dataformat)
        if data is not None:
            clear()
            main(data)
    else:
        print(RED + BOLD + "No valid input provided. Exiting." + RESET)