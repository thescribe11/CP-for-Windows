import os
import sys
from getpass import getuser
import shutil

def main() -> int:
    try:
        to_copy = sys.argv[1]
        destination = sys.argv[2]
    except:
        sys.stderr.write("Excuse me, but I am afraid that you are using this command wrong.\n")
        sys.stderr.write("The correct usage is: cp <path> <destination path>")
        sys.exit(1)

    to_copy = to_copy.replace('~', f"C:\\Users\\{getuser()}")
    destination = destination.replace('~', f"C:\\Users\\{getuser()}")
    
    with open(to_copy, 'rb') as f:
        contents = f.read()
    with open(destination, 'wb') as f:
        f.write(contents)

    return 0

if __name__ == "__main__":
    main()