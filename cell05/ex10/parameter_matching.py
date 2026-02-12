#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    keyword = sys.argv[1]
    text = input("What was the parameter? ")

    if text == keyword :
        print("Good job!")
    else:
        print("Nope, sorry...")