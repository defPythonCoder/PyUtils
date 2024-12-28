from os import name, system, environ, pathsep
import os
import sys

sys.exit("Still IN development")

if name != "nt":
    sys.exit("\033[91m"+"Feature only for Windows.")

if len(sys.argv) > 1:
    working_dir = sys.argv[1]
    os.chdir(working_dir)