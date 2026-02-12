#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("none")
else :
    params = sys.argv[1:]
    print("parameters:", len(params))

    for item in params :
        print(item + ":", len(item))