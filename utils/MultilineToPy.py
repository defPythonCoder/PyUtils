from os import system, name

# ANSI color codes for styling
RESET = "\033[0m"
BOLD = "\033[1m"
WHITE = "\033[97m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"

def clear():
    system("cls" if name == "nt" else "clear")

def display_instructions():
    instructions = [
        f"{BOLD}{BLUE}Welcome to the Multiline Input Formatter!{RESET}",
        f"{GREEN}This tool allows you to format multiline input dynamically.{RESET}",
        f"{CYAN}Options:{RESET}",
        f"{YELLOW}- Format as a Python list assigned to a variable.{RESET}",
        f"{MAGENTA}- Format as individual print statements.{RESET}"
    ]

    for line in instructions:
        print(line)

def get_multiline_input():
    """Prompts the user for multiline input, ending on double Enter."""
    print(MAGENTA + BOLD + "\nProvide your multiline input. Submit by pressing Enter twice." + RESET)
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    return lines

# Format data as a Python list
def format_as_list(var_name, data):
    """Formats data into a Python list assigned to a variable."""
    print(GREEN + f"\nFormatting as list for variable: {var_name}" + RESET)
    indent = " " * (len(var_name) + 4)
    for i, line in enumerate(data):
        if i == 0:
            print(f"{var_name} = ['{line}',")
        elif i == len(data) - 1:
            print(f"{indent}'{line}']")
        else:
            print(f"{indent}'{line}',")

# Format data as print statements
def format_as_print_statements(data):
    """Formats data as a sequence of Python print statements."""
    print(GREEN + "\nFormatting as individual print statements:" + RESET)
    for line in data:
        print(f"print('{line}')")

# Display input formatting options
def display_input_choices():
    """Displays input formatting options to the user."""
    print(CYAN + BOLD + "\nChoose how you would like to format the input:" + RESET)
    print(YELLOW + "1. As a Python list assigned to a variable." + RESET)
    print(YELLOW + "2. As multiple Python print statements." + RESET)

# Handle user choice
def handle_user_choice(data):
    """Handles the user's choice for formatting the input."""
    display_input_choices()
    choice = input(CYAN + BOLD + "\nEnter your choice (1 or 2): " + RESET)

    if choice == '1':
        var_name = input(GREEN + BOLD + "\nEnter the variable name: " + RESET)
        clear()
        format_as_list(var_name, data)
    elif choice == '2':
        clear()
        format_as_print_statements(data)
    else:
        print(RED + BOLD + "\nInvalid choice. Please restart the program and try again." + RESET)

# Main function to execute the program flow
def main():
    """Main function to execute the program flow."""
    clear()
    display_instructions()
    data = get_multiline_input()
    clear()
    handle_user_choice(data)

if __name__ == "__main__":
    main()
