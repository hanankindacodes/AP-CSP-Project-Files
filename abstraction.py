#Abstraction

#Intro
#2 Parameters (name of user, name of game)
#Introduce user to your game

def intro(user_name, game_name):
    print("Hey there " + user_name + ("! Welcome to " + game_name  + ("!")))

#Outro
#2 Parameters (Name of user, name of game)
#Say Goodbye to user

def outro (user_name, game_name):
    print("See you next time " + user_name + ("!"))
    
intro("Hanan", "Monopoly")
outro("Hanan", "Monopoly")