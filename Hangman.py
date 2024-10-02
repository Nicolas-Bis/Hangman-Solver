import random
from WordList import allWords

def getRandomWord():
    return random.choice(allWords).lower() #Chooses random word

def displayWord(word, correctLetters):
    return " ".join([letter if letter in correctLetters else '_' for letter in word]) #Display current word

def play_hangman():
    word = getRandomWord()
    correctLetters = set()
    wrongLetters = set()
    lives = 6

    print('Welcome to Hangman!')

    while lives > 0:
        print(f'\nWord: {displayWord(word, correctLetters)}')
        print(f"Wrong letters: {', '.join(wrongLetters)}")

        guess = input('Guess a letter: ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print('Invalid value.')

        elif guess in correctLetters or guess in wrongLetters:
            print('Try another letter.')

        elif guess in word:
            correctLetters.add(guess)
        else:
            wrongLetters.add(guess)
            lives -= 1

        if set(word) == correctLetters:
            print(f'You win! The word was: {word}')
            break

    if lives == 0:
        print(f'You died! The word was: {word}')

play_hangman()
