#Hanan Mohamed
#10/18/23
#Quiz Grader
quiz = int(input("What grade did you get on your quiz?: " )) 
average = sum(quiz)/count(quiz)
if (average <=59):
    print("F")
elif (average <=69):
    print("D")
elif (average <=79):
    print("C")
elif (average <=89):
    print("B")
elif (average <=100):
    print("A")