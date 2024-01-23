#Hanan Mohamed
#10/18/23
#Quiz Grader

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

grader()