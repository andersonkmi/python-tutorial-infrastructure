#!/usr/bin/env python3
import sys

def main():
    if len(sys.argv) < 3:
        print("Usage: ccwc.py <option> <file>")
        print("Options: -c, -l, -w, -m")
        sys.exit(1)

if __name__ == "__main__":
    main()