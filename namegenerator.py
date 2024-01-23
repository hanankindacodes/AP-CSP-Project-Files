#Hanan Mohamed
#10/24/23
#Vacation Spot Generator

def vacationGenerator ():
    print("Hey there! Welcome to Your Favorite Vacation Spot Generator.")
    print("After answering the following questions, we will provide you with the perfect vacation spot.")
    ans = input("summer (s) or winter(w)?: ")


    #final answers should be really happy phrases and different for each input that user uses
    #chunk of questions and answers organized if user inputs summer
    if ans == "s": 
        ans = input("water (w) or sand (s)?: ")
        if ans =="w":
            ans = input("adventure (a) or relaxations (p)?: ")
            if ans == "a":
                print ("Bring in the shades, we're heading to Bora Bora!")
            if ans == "p":
                print ("Relaxation at the Malidives it is!")
        if ans =="s":
            ans= input ("trees (t) or flowers(f)?: ")
            if ans == "t":
                    print ("Arizona, here we come!")
            else:
                print ("Lets go to Colombia!")

    #chunks of questions and answers if user inputs winter
    if ans =="w":
        ans = input ("serenity (s) or excitement (e)?: ")
        if ans == "s":
            ans=input("plants (p) or animals (a)?: ")
            if ans == "p":
                print("Have fun in Iceland!")
            if ans == "a":
                print ("Someone book a flight to Alaska ASAP!")
        if ans == "e":
            ans=input("city (c) or country (co)?: ")
            if ans =="c":
                print ("Always wanted to go to Seoul, South Korea!")
            if ans== "co":
                print("Oooh, Switzerland we go!")

vacationGenerator()