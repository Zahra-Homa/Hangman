import random

words = ["python", "challenge", "variable",                    # provide the game with a List of words 
    "function", "condition", "project","syntax", 
    "debug",  "program", "string", "boolean", "operator"]

figures = {0: (" _____ ",                                      # ASCII art for hangman stages
               "   |   ",
               "       "),
           1: (" _____ ",
               "   |   ",
               "   O   "),
           2: (" _____ ",
               "   |   ",
               "   O   ",
               "   |   "),
           3: (" _____ ",
               "   |   ",
               "   O   ",
               "  /|   "),
           4: (" _____ ",
               "   |   ",
               "   O   ",
               "  /|\\  "),
           5: (" _____ ",
               "   |   ",
               "   O   ",
               "  /|\\  ",
               "  /    "),
           6: (" _____ ",
               "   |   ",
               "   O   ",
               "  /|\\  ",
               "  / \\   ")}

answer_word = random.choice(words)                           # Randomly select a word from the list

remaining_mistakes = 6                                       # Number of allowed mistakes

hidden_word = ['_' for _ in answer_word]                     # Create a hidden version of the word with underscores

while remaining_mistakes > 0 and '_' in hidden_word:         # Main game loop: continues until the player runs out of chances or guesses the word
    picked_letter = input("\nPick a letter:")                # Ask the player to pick a letter
    
    if picked_letter in answer_word:
        print(f"CORRECT! The word contains the letter {picked_letter}!")
        for i,j in enumerate(answer_word):                   # Reveal the guessed letters in the hidden word
            if picked_letter == j:
                hidden_word.pop(i)
                hidden_word.insert(i , j)
        print(f"hidden_word: {' '.join(hidden_word)}")
       
    else:                                                   # Reduce the number of remaining mistakes
        remaining_mistakes -= 1
        print(f"WRONG! Number of mistakes left: {remaining_mistakes}.")
        print(f"hidden_word: {' '.join(hidden_word)}")
        for line in figures[6-remaining_mistakes]:          # Display the hangman figure according to the number of mistakes
            print(line)
        
else:                                                       # End of game messages
    if remaining_mistakes == 0:
        print("\nHANGED!!")
    elif '_' not in hidden_word:
        print("\nCONGRATES!! You guessed the word correctly!")
