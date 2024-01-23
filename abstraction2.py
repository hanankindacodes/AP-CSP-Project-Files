#Hanan Mohamed
#Abstraction 2

#Functions
def intro(user_name, game_name):
    print("Hey there " + user_name + ("! Welcome to " + game_name  + ("!")))

def grader ():
    quiz = int(input("What grade did you get on your quiz?: " )) 
    if (quiz <=59):
        print("F")
    elif (quiz <=69):
        print("D")
    elif (quiz <=79):
        print("C")
    elif (quiz <=89):
        print("B")
    elif (quiz <=100):
        print("A")

def outro (user_name, game_name):
    print("See you next time " + user_name + ("!"))

#Main
intro ("Hanan", "grader")
grader()
outro("Hanan", "grader")
