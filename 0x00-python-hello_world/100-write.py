#!/usr/bin/python3

import sys

def main():
    # Writing the message to standard error output
    sys.stderr.write("This piece of art is quite useful - Dora Korpar, 2015-10-19\n")
    # Exiting with status code 1
    exit(1)

if __name__ == "__main__":
    main()

