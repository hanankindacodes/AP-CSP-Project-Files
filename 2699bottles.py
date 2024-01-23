# Yingyi, Hanan
# AP CSP Pd 4
# 11/27/2023




# To print the lyrics to 99 Rootbeers with a for loop
# No parameters
def rootbeer_lyrics():
    x = 100
    # the loop to change number of rootbeers
    for i in range(100):
        x = x-1
        # for when rootbeers run out
        if x == 0:
            print("No more bottles of rootbeer on the wall.\n\n")  #Once the number of rootbeers reach 0, there's a different comment necessary "no more bottles"
            print("""
  .   *   ..  . *  *
*  * @()Ooc()*   o  .
    ()Q@*0CG*O()  ___
   |\_________/|/ _ \
   |  |  |  |  | / | |
   |  |  |  |  | | | |
   |  |  |  |  | | | |
   |  |  |  |  | | | |
   |  |  |  |  | | | |
   |  |  |  |  | \_| |
   |  |  |  |  |\___/
   |\_|__|__|_/|
    \_________/
""")
        
        elif x == 1: 
            print(str(x) + " bottle of rootbeer on the wall, " +str(x)+  " bottle of rootbeer. Take one down and pass it around, " + str(x-1) + " bottle of beer on the wall.\n")
        #This writes the comment specifically for when x is 1 so "bottle" is singular
        else:
            print(str(x) + " bottles of rootbeer on the wall, " +str(x)+  " bottles of rootbeer. Take one down and pass it around, " + str(x-1) + " bottles of beer on the wall.\n")#This is for all the other verses in which the same words are repeated and "bottle" is plural




rootbeer_lyrics()
