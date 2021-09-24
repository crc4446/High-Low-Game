#This program will let a user play the high/low game
#Created by: Chris Caponi
gamesPlayed = 0 ###############################
gamesWon = 0 #used to calculate end results#  
winPerc = 0 ###############################
again = True
             #the program will repeat upon player input
while again: 

    import random
    secret = random.randrange(1,64) #the program will generate a random # from 1-64 inclusive.
    print("I am thinking of a number in the range of 1-64 inclusive.")
    print("You have 7 tries to guess it.")
    guess = int(input("What is your guess? "))
    guesses = 1 #keeps track of number of guesses
    print(secret)
    

        
    for x in range(1,8): #the following code will only repeat 7 times.
        while (guess < 1 or guess > 64): #prevents player from moving on thru the game until entering valid input.
            guess = int(input("Your guess was outside the range, try again. "))
        if (guess == secret): #when player guesses correct number, they recieve the following message w/ how many attempts it took. 
            print("Congrats, you are a winner in", guesses, "tries!!")
            gamesWon = gamesWon + 1 #adds a win after guessing the correct number.
            break
        elif (guess > secret): #provides hints as to wether or not the player guessed too high.
            print("Sorry, your guess was too high.")
            guesses = guesses + 1 #tracks each attempt.
            if (guesses == 8):
                break
            else:
                guess = int(input("What is your guess? "))
        elif (guess < secret): #provides hints as to wether or not the player guessed too low.
            print("Sorry, your guess was too low.")
            guesses = guesses + 1 #tracks each attempt.
            if (guesses == 8):
                break
            else:
                guess = int(input("What is your guess? "))

    gamesPlayed = gamesPlayed + 1        #######################
    winPerc = (gamesWon/gamesPlayed)*100 #Formulas for end game#
                                         #######################   
    if (guess == secret): #if player guesses the number, they will be asked to play again.
        answer = input("Enter yes to play again, anything else to quit. ")
        if (answer != "yes"): #if they choose to not play again, player will recieve win/loss ration and percentage.
            again = False
            print("You won {} out of {} for a winning percentage of {:.3f}%".format(gamesWon, gamesPlayed, winPerc))
    elif (guesses == 8): #if player runs out of attempts, they will be asked if they want to play again.
        print("YOU LOSE!!", "The number was",secret)
        answer = input("Enter yes to play again, anything else to quit. ")
        if (answer != "yes"): #if they choose to not play again, player will recieve win/loss ration and percentage.
            again = False
            print("You won {} out of {} for a winning percentage of {:.3f}%".format(gamesWon, gamesPlayed, winPerc))
        
        
print(input("press enter to exit."))

    
            
            
    

    
    
    
        
        
            
