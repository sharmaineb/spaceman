import random 

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r') # name of file we want to open
    words_list = f.readlines() # takes each line from the words.txt file and stores it in a list
    f.close() # remember to close the open file
    
    words_list = words_list[0].split(' ') # comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list) # returns a random word from list
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    """checks if the letters the user inputs is in the secret word that is a random word from word list.
       parameters:
       secret_word (string): the random word in 'words.txt' that the user is trying to guess
       letters_guessed (list of strings): list of letters the user has guessed so far.
       returns:
       True is the letters guessed are in the secret word and False if they aren't."""

    counter = 0 # set variables to 0 so it can be filled with data
    correct_letters = 0 # set variables to 0 so it can be filled with data
    for letter in secret_word: # loop 
        if letter in (letters_guessed):
            correct_letters += 1
            return False
        else:
            counter += 1
            return True # return bool
    

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet

    """function that shows the letters the user has inputed and displaying underscores for thr letters that have not been guessed yet.
       parameters:
       secret_word(string): the random word in 'words.txt' that the user is trying to guess.
       letters_guessed (list of strings): list of letters the user has guessed so far.
       returns:
       letters and underscores as strings. if the user guesses the letter correctly the underscore will be replaced with the correct letter."""
    
    correctly_guessed = " " # letters the user has correctly inputed

    for letter in secret_word:
        if letter in letters_guessed:
            correctly_guessed += letter # letters that are correct will replace blanks
        else: correctly_guessed += " _ " # underscore for letters that haven't been guessed yet.
    return correctly_guessed

def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word

    """function that checks if the letter the user inputed is in the secret word which is a random word from 'words.txt'.
       parameters:
       guess (string): the letter the user has guessed in the current round.
       secret_word (string): the random word in 'words.txt' that the user is trying to guess.
       returns:
       True if the letter the user has guessed is in the secret_word and False otherwise."""

    if guess in secret_word: # check if the letter guess is in the secret word
        return True # return bool
    else:
        return False


def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
    secret_word (string): the secret word to guess.
    '''
    
    """the function that controls the game - spaceman.
       parameters:
       secret_word (string) the random word in 'words.txt' that the user is trying to guess."""
    
    letters_guessed = [] # list for letters player has guessed
    chances = 7 # when uses all 7, game breaks
    print("Let's Play Spaceman!")
    print("You will be given only 7 incorrect guesses.")
    print("Please only enter one letter at a time.")

    playing = True # game loop
    while playing:
        guess = input("Enter a Letter: ")
        print("--------------------------------------------------")
        if is_guess_in_word(guess, secret_word):
            print("You guessed a correct letter!")
            letters_guessed.append(guess)
            print(f"Your List of Used Letters: {letters_guessed}")
        else:
            chances -= 1 # if player guesses a wrong letter, the number of times to get answer wrong goes down by one
            print(f"{guess} is incorrect. You have {chances} guesses remaining.") # show player how many wrong guesses left when they input an incorrect letter
            letters_guessed.append(guess)
            print(f"Your List of Used Letters: {letters_guessed}") # shows player the letters they've used
        print(get_guessed_word(secret_word, letters_guessed))

        if is_word_guessed(secret_word, letters_guessed): # when player runs out of wrong guesses 
            if chances == 0:
                print(f"I'm sorry, but you've ran out of guesses. The correct word was {secret_word.upper()}") # end game and show the word
                playing = False
                break # end game

#These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)




# used cli-games as a reference for game loop






#TODO: show the player information about the game according to the project spec
#TODO: Ask the player to guess one letter per round and check that it is only one letter
#TODO: Check if the guessed letter is in the secret or not and give the player feedback
#TODO: show the guessed word so far
#TODO: check if the game has been won or lost









    