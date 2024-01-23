#Hanan Mohamed
#12/01
#Leap Year Checker


#Functions
def is_leap_year(year):
    if (year % 4 == 0) and not (year % 100==0): #As long as its divisble by 4 and not 100 its already True
        return True
    elif (year % 100==0) and not (year % 400==0): #I have to make sure that its not just divisble by 100 but it can't be divisible by 400 to be false
        return False
    elif (year % 400==0): #if it is divisible by 400 then it also counts as true
        return True
    else:
        return False

#Main
print(is_leap_year(2000))
print(is_leap_year(2022))
print(is_leap_year(2024))
