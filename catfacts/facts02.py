#!/usr/bin/env python3

import requests

def main():
    r = requests.get("https://cat-fact.herokuapp.com/facts")
    
    for catfact in r.json()["all"]:
        print(catfact.get("text"))

main()
