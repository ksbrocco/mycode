#!/usr/bin/env python3

people= [{"name": "Christina Koch", "craft": "ISS"}, {"name": "Alexander Skvortsov", "craft": "ISS"}, {"name": "Luca Parmitano", "craft": "ISS"}, {"name": "Andrew Morgan", "craft": "ISS"}, {"name": "Oleg Skripochka", "craft": "ISS"}, {"name": "Jessica Meir", "craft": "ISS"}]

a = 0
for i in people:
    print(people[a].get("name") + " is on the " + people[a].get("craft"))
    a += 1
    


