#!/usr/bin/env python3

char_name = input("Which character do you want to know about? (Flash, Batman, Superman)? ")
char_stat = input("What statistic do you want to know about? (Strength, Speed, or Intelligence)? ")
char_dict = {"Flash":{"Speed": "Fastest", "Intelligence": "Lowest", "Strength": "Lowest"}, "Batman":{"Speed": "Slowest", "Intelligence": "Highest", "Strength": "Money"}, "Superman":{"Speed": "Fast", "Intelligence": "Average", "Strength": "Strongest"}}

print(f"{char_name}'s {char_stat} is: {char_dict[char_name][char_stat]}")

