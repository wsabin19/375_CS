#This is a guessing game where the computer has a number and the user has to guess it
import random
def main():
    print("Im thinking of a number between 1 and 20")

    magic_number = random.randrange(1,20)
    guess = 0
    attempts = 0
#the above three lines are the variables
#the line setting "magic_number" is making use of the random function from a scale of 1 to 20
    while guess != magic_number :
        guess = eval(input("Guess the Magic Number:"))
#The lines 14-17 are giving hints if the number the user prompted is above or below the "magic Number"
        if guess < magic_number:
            print ("Too low!")
        elif guess > magic_number:
            print ("Too High")
        else :
            print ("You Guessed Correctly!")
        attempts =  attempts + 1
    print ("You got it! it only took you", attempts, "attempts")


main()
