#!/usr/bin/env python3

import os, fnmatch

def find(pattern, path):
    result = []
    for root, dirts, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

lookfor = input("What am I looking for? ")
lookwhere = input("What is the path in which I should search? ")

a = find(lookfor, lookwhere)

for x in a:
    print(x)
