#Hanan Mohamed
#12/05
#MadLibs

#Init
#Functions
name = input("Write any name: ") #Description: the person creates the character name for the story
feet = input("Enter any number: ") #Description of character: height
color = input("Input a color: ") #Description of character: hair color
verb = input ("Write in a verb (w/o -ing): ") #Description of character: hobby/enjoyed activity
location = input ("Write the first location that comes to mind: ") #The last place the character was last seen because the story is about them being lost
days = input("Write a different number: ") #Amount of days the character was lost
emotion = input("Enter an emotion: ") #Emotion of character when they see their friend
adjective = input("Input an adjective of choice: ") #Description: just an adjective

#Main
#Here's the entire story with capitalized and bolded inputs
print(("Hey there! I am looking for my lost friend ") +('\033[1m' + name.upper() +'\033[0m') + (". Could you help me find them? They're ") + ('\033[1m'+ feet.upper() +'\033[0m')+ (" feet tall, have ") +('\033[1m'+ color.upper() + '\033[0m') +(" colored hair, and love to ") + ('\033[1m'+ verb.upper() +'\033[0m') + (". The last place I saw ") + ('\033[1m'+ name.upper() +'\033[0m') + (" was ") + ('\033[1m'+ location.upper() +'\033[0m') +(", about ")+ ('\033[1m'+ days.upper() +'\033[0m') + (" days ago. Wait, who's that over there? It's ") + ('\033[1m'+ name.upper() + '\033[0m') + ("! ") + ('\033[1m' + name.upper() + '\033[0m') + (" is so ")+ ('\033[1m' + emotion.upper() +'\033[0m') + (" to see me. Thanks for helping me find my ") + ('\033[1m'+ adjective.upper() + '\033[0m') + (" friend."))