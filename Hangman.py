import random
FILENAME = '5000EnglishWords.txt'

# Read words from txt file
def loadWordsFromFile(filename):
    with open(filename, 'r') as file:
        words = file.read().splitlines()  # Remove newline characters
    return words


def getRandomWord(wordList):
    return random.choice(wordList).lower() # Choose random word

def displayWord(word, correctLetters):
    return " ".join([letter if letter in correctLetters else '_' for letter in word]) #Display current word

# SOLVER Shows the possible words
def filterPossibleWords(word, correctLetters, wrongLetters, wordList):
    filteredWords = []
    for w in wordList:
        # Step 1: Filter by word length
        if len(w) != len(word):
            continue

        # Step 2: Check if letters are in correct positions
        match = True
        for i in range(len(word)):
            if word[i] in correctLetters and w[i] != word[i]:
                match = False
                break

        if not match:
            continue

        # Step 3: Remove words that contain wrong letter
        if any(wrongLetter in w for wrongLetter in wrongLetters):
            continue

        filteredWords.append(w)

    return filteredWords

def play_hangman():
    wordList = loadWordsFromFile(FILENAME) # Load words

    word = getRandomWord(wordList)
    correctLetters = set()
    wrongLetters = set()
    lives = 6

    # Initialize all possible words for list
    possibleWords = wordList

    print('Welcome to Hangman!')

    while lives > 0:
        print(f'Word: {displayWord(word, correctLetters)}')
        print(f"Wrong letters: {', '.join(wrongLetters)}")

        # Filter words
        possibleWords = filterPossibleWords(word, correctLetters, wrongLetters, possibleWords)
        print(f"SOLVER {len(possibleWords)} words:  {', '.join(possibleWords)}") # List all possible words

        guess = input('\nGuess a letter: ').lower()

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
