# Names: Hanan Mohamed
# Date: 12/13/23
# Pokemon Simulator

# Initialize


# Global variables
pokemon_level = 0
pokemon_name = "Charmander"

# Functions              
pokemon_name = input("What is your Charmander's name?: ")
def pokemon_game():
    def train_pokemon():
            global pokemon_level
            pokemon_level = int(pokemon_level) + 1
            print(pokemon_level)
 
    def battle_pokemon():
            global pokemon_level
            pokemon_level = int(pokemon_level) + 2
            print(pokemon_level)

    def display_pokemon():
            global pokemon_level
            global pokemon_name
            print(pokemon_name)
            print(pokemon_level)
                
    def evolve_pokemon():
            global pokemon_level
            global pokemon_name
            if int(pokemon_level) <5 :
                print("You're not ready to evolve yet :(. Train or Battle to increase your level! )")
            if int(pokemon_level) >= 5 and int(pokemon_level) > 10:
                print("Your Charmander is now a Charmeleon! ")
                pokemon_name == "Charmeleon"
            elif int(pokemon_level) >= 10:
                print("Your Charmeleon is now a Charizard! ")
                pokemon_name == "Charizard"
            
    menu = int(input(" 1) Train\n 2) Battle\n 3) Display\n 4) Evolve\n 5) Exit\n Please choose an option: "))
    if menu ==1:
        train_pokemon()
    if menu ==2:
        battle_pokemon()
    if menu ==3:
        display_pokemon()
    if menu == 4:
        evolve_pokemon()
    else:
        quit()  
    
# Main
while True:
    pokemon_game()