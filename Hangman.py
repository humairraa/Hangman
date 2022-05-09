'''
problem: 
A word guessing game of hangman will be played through simple user input. User will be prompted to guess a random word each time they run the game. Every wrong input of the letter would result in a subtraction of the user's life out of 10. once the user runs out of all 10 lives,  the game will show that the user has lost the game and will reveal the word the user was guessing. if the user guesses the word within the 10 chances they get, the game will show that the user has won.

plot twists - 
Though the user will not be able to play the word guessing game if their name has been left blank and if they are under the age of 18.

When guessing the word, if the user accidentally inputs anything other than a letter. a new loop would begin where they would have to guess the same word again with the remaining life they have left. 
'''

import random #imports the random library on python so random.choice function runs smoothly

name = input("What would you like to be called? ")
age = input("how old are you? ") 
empty = "" #code for loop as the end
extra = str("-" or "," ) #code for loop as the end


def intro(phrase): #game rules funtion
    print("-", phrase) #all the rules will start with -
    return

# game rules 
intro("HOW TO PLAY:")
intro("Welcome to the game guessing by Humaira.")
intro("RULES: ")
intro("In this game, you will be given a random word from Humaira's words list.")
intro("You will have 10 chances to guess a random letter, and each time you get a letter wrong, the chances of your guesses will decrease.")
intro("The goal of this game is to guess the random word given to you within the 10 chances you get.")
print("Good Luck!", name + "!")
print(" ")


#words = ['wifi']
words = ['wifi', 'picture', 'house', 'iphone', 'python', 'math', 'blanket', 'hands', 'game', 'books', 'sun', 'moon'] #these are the list of words that the user would be given.
word = random.choice(words) #will pick a random letter from the list

guesses = '' #letters user has guessed but get added to the empty string
lives = 10 #the amount of wrong guesses the user has.

while lives > 0: 
    missed = 0 #if user does not guess the letter this will increase by 1
    
    while name!= empty  and int(age) >= 18: #players over 18 and a name could play
        print("welcome", name)
        break 
    else:
        print("u cant play LOL")
        break  #will not continue the game any further if age is less than 18  

    for letter in word: 
        if letter in guesses:         
            print(letter, end = " ")  # will print the leffer, if correct          
        else: 
            print("_", end = " ")
            missed += 1 #if letter is not correct one life will be taken down
    
    print("") 
    
    if missed == 0: # if they win, this will be said.
        print("CONGRAGULATIONS!!!!!") 
        print("You guessed the word", word, "correct!") 
        print("Here is your crown ♛", name + "!")
        break
     
    print("")   
    guess = input("Input a letter: ")
    guesses += guess
    print("")
    
    while (not guesses.isalpha()): #only letters.
        guesses = input("***INVALID CHARACTER*** Input a letter again: ")       
       
        for letter in word: #new loop for the plot twist of inputting anying other than a letter starts
            if letter in guesses: 
                print(letter, end = " ") 
            else: 
                print("_", end = " ")
                missed += 1                
            
    print("")
    if guess not in word: # if letter not in the word they are guessing the following things will be said.
        lives -= 1
        print("The letter you have chosen is an incorrect letter and is not in the word. Try again.")
        print("Lives left: ", lives) #only shown when when theres an incorrect letter.
        cc = "you have guessed the letters: {}".format(guesses) 
        print(cc)
        print(" ")
    
        if lives == 0: #if they lose, this will be said.
            print("You've run out of guesses.")
            print("Sorry for the loss", name, "but heres a cookie 🍪 ")
            print("The word was {}".format(word) + "!") 


if name == empty: 
    name = False 
    print("Ty..") # will be printed if name it not given
elif name == extra: 
    name = False 
    print("Thanks for playing loll.") #if a "-" or "," is the input as a name this will be said
else:
    print("Thankyou for playing.") #if a letter will be given as a name, this will print
    
