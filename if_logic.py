#!/usr/bin/env python3

#This program will recommend a car based on your selections.

#Dictionary based on a limited number of cars
car_dict = {"Compact":{"Honda": "Civic", "Hyundai": "Elantra", "Toyota": "Corolla", "Nissan": "Sentra"}, "Midsize":{"Honda": "Accord", "Hyundai": "Sonata", "Toyota": "Camry", "Nissan": "Altima"}}
#Intro message
print("This program will recommend a car to you based on your selection. Disclaimer: The choices are case sensitive.")

#Infinite loop to force the user to make a valid selection
while True:
    #Receives the car type and runs through the first If else statements
    car_type = input("Please choose a car type. (Compact or Midsize) ")
    #Moves into the next loop and if else statement if Compact is written
    if car_type == "Compact":
        #2nd infinite loop to force a valid selection
        while True:
            #Receives the car brand and runs through the 2nd set of if else statements
            car_brand = input("Please choose a car brand. (Honda, Hyundai, Toyota, or Nissan) ")
            #Compares the car brand input to the keys in the dictionary. If there is no match it makes you select again.
            if car_dict.get(car_type, car_brand).get(car_brand) == None:
                print("Invalid Selection, try again.")
            #If there is a key it will run this else statement
            else:
                #Prints the recommendation utilizing all the variable and dictionary
                print(f"We recommend you buy a {car_brand} {car_dict[car_type][car_brand]}.")
                #Breaks out of the loop after the recommendation
                break
        #Breaks out of the first loop so it doesn't ask for the car type again    
        break
    #See comments above as its the same as the choice for Compact cars
    elif car_type == "Midsize":
        while True:
            car_brand = input("Please choose a car brand. (Honda, Hyundai, Toyota, or Nissan) ")
            if car_dict.get(car_type, car_brand).get(car_brand) == None:
                print("Invalid Selection, try again.")
            else:
                print(f"We recommend you buy a {car_brand} {car_dict[car_type][car_brand]}.")
                break
        break
    #Forces you to enter a new selection until you pick Compact or Midsize
    else:
        print("Invalid selection, try again.")


