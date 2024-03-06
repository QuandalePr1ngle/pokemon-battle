
print("")
print("                                  ,'\\")
print("    _.----.        ____         ,'  _\   ___    ___     ____")
print("_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.")
print("\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |")
print(" \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |")
print("   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
print("    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |")
print("     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |")
print("      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |")
print("       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |")
print("        \_.-'       |__|    `-._ |              '-.|     '-.| |   |")
print("                                `'                            '-._|")
print("")
print("Pokemon Battle")
print("")
x = 0

import json
import random

# read Pokemon file into dictionary
pokemons_file = open('pokemons.json') # opening JSON file
pokemons = json.load(pokemons_file) # returns JSON object as a dictionary
pokemons_file.close() # Closing file

print(pokemons[0])

while True:
    print("1. Show pokemon by index")
    print("2. Top 10 strongest pokemons (by total)")
    print("3. Top 10 weakest pokemons (by total)")
    print("4. Battle of 2 pokemons")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        index = input("Enter a number (1-43): ")
        number = int(index) - 1
        print(pokemons[int(number)])
        pass
        # https://www.w3schools.com/python/python_dictionaries_access.asp
    elif choice == '2':
        def TenStrongest(pokemon):
            return int(pokemon["total"])
        pokemons.sort(key = TenStrongest, reverse = True)
        while x < 10:
            x = x + 1
            print(pokemons[:x])
        pass
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '3':
        # https://www.w3schools.com/python/python_lists_sort.asp
        pass
    elif choice == '4':
        # Battle
        # 
        # https://www.w3schools.com/python/ref_random_choice.asp - random choice
        # Computer choosing one random Pokemon from list
        # Player choosing by entering Pokemon index
        # Damage is calculated by: (attack of Pokemon 2) - (defense of Pokemon 1) + (random from 5 to 20), and vice-versa
        # Player reaching 0 health (total) - lost
        pass

    elif choice == '5':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 5")

    print("==========================")


