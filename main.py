import os
import sys
import subprocess
import time
from random import randint

VERSION = "1.2.2"

# Default working directory
working_dir = sys.argv[1] if len(sys.argv) > 1 else None

# ANSI color codes for professional styling
RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
UNDERLINE = "\033[4m"
WHITE = "\033[97m"
GRAY = "\033[90m"
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"

# Clear the console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Display the banner with a professional design
def display_banner():
    banners = [[" ██▓███  ▓██   ██▓ █    ██ ▄▄▄█████▓ ██▓ ██▓      ██████ ",
                "▓██░  ██▒ ▒██  ██▒ ██  ▓██▒▓  ██▒ ▓▒▓██▒▓██▒    ▒██    ▒ ",
                "▓██░ ██▓▒  ▒██ ██░▓██  ▒██░▒ ▓██░ ▒░▒██▒▒██░    ░ ▓██▄   ",
                "▒██▄█▓▒ ▒  ░ ▐██▓░▓▓█  ░██░░ ▓██▓ ░ ░██░▒██░      ▒   ██▒",
                "▒██▒ ░  ░  ░ ██▒▓░▒▒█████▓   ▒██▒ ░ ░██░░██████▒▒██████▒▒",
                "▒▓▒░ ░  ░   ██▒▒▒ ░▒▓▒ ▒ ▒   ▒ ░░   ░▓  ░ ▒░▓  ░▒ ▒▓▒ ▒ ░",
                "░▒ ░      ▓██ ░▒░ ░░▒░ ░ ░     ░     ▒ ░░ ░ ▒  ░░ ░▒  ░ ░",
                "░░        ▒ ▒ ░░   ░░░ ░ ░   ░       ▒ ░  ░ ░   ░  ░  ░  ",
                "          ░ ░        ░               ░      ░  ░      ░  ",
                "          ░ ░                                            "],
               ["██████  ██    ██ ██    ██ ████████ ██ ██      ███████ ",
                "██   ██  ██  ██  ██    ██    ██    ██ ██      ██      ",
                "██████    ████   ██    ██    ██    ██ ██      ███████ ",
                "██         ██    ██    ██    ██    ██ ██           ██ ",
                "██         ██     ██████     ██    ██ ███████ ███████ "],
               ['██████╗ ██╗   ██╗██╗   ██╗████████╗██╗██╗     ███████╗',
                '██╔══██╗╚██╗ ██╔╝██║   ██║╚══██╔══╝██║██║     ██╔════╝',
                '██████╔╝ ╚████╔╝ ██║   ██║   ██║   ██║██║     ███████╗',
                '██╔═══╝   ╚██╔╝  ██║   ██║   ██║   ██║██║     ╚════██║',
                '██║        ██║   ╚██████╔╝   ██║   ██║███████╗███████║',
                '╚═╝        ╚═╝    ╚═════╝    ╚═╝   ╚═╝╚══════╝╚══════╝']]
    selected_banner = banners[randint(0, len(banners) - 1)]
    print(f"{BOLD}{CYAN}", end="")
    for line in selected_banner:
        print(line)
    print(f"{DIM}Version: {WHITE}{VERSION}{RESET}")
    print(f"{GRAY}Developed by: Python Coder{RESET}")
# List Python files in the 'utils' directory
def list_python_files():
    utils_dir = "utils"
    if not os.path.exists(utils_dir):
        print(f"{RED}Error:{RESET} The 'utils' directory does not exist. Please create it and add Python files.")
        return []

    files = [f for f in os.listdir(utils_dir) if f.endswith(".py")]
    if not files:
        print(f"{YELLOW}Notice:{RESET} No Python files found in the 'utils' directory.")
    return files

# Display menu and execute the selected file
def run_menu(files):
    print(f"\n{BOLD}{WHITE}Available Tools:{RESET}")
    for idx, file in enumerate(files, start=1):
        print(f"  {GREEN}[{idx}] {BLUE}{file.replace('.py', '')}{RESET}")

    print(f"\n{CYAN}Enter the tool number to execute, or '0' to exit.{RESET}")
    try:
        choice = int(input(f"{BOLD}{UNDERLINE}Your Choice:{RESET} "))
        if choice == 0:
            print(f"{YELLOW}Exiting PyUtils. Have a productive day!{RESET}")
            return

        if 1 <= choice <= len(files):
            script_path = os.path.join("utils", files[choice - 1])
            print(f"\n{MAGENTA}Executing {WHITE}{files[choice - 1]}{RESET}{MAGENTA}...{RESET}\n")
            time.sleep(1)
            clear()
            subprocess.run(["python", script_path, working_dir] if working_dir else ["python", script_path])
        else:
            print(f"{RED}Invalid choice.{RESET} Please select a valid option from the menu.")
    except ValueError:
        print(f"{RED}Error:{RESET} Please enter a numeric value.")

# Main program flow
def main():
    clear()
    display_banner()
    files = list_python_files()
    if files:
        run_menu(files)

if __name__ == "__main__":
    main()
