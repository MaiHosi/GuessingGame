import os
import random
from StringDatabase import read_words
from Game import Game


class Guess:
    
    def __init__(self, mode):
        self.mode = mode
        self.games_played = []
        self.test = mode
        self.fileName = "four_letters.txt"
        self.quit_game = False
        self.total_score = 0
        

    def start_game(self):
        while not self.quit_game: #create a new game with a new random word
            quit_round = False
            words = read_words(self.fileName)

            if words:
                current_word = random.choice(words)

            g = Game(current_word)

            while not quit_round:
                print("++")
                print("++ The Great Guessing Game!")
                print("++\n")

                display_guess = ''.join(c if c.lower() in g.correctLetters else '-' for c in current_word)
                if self.test == "test":
                    print(f"Current Word: {current_word}")
                print("Current Guess: ", display_guess )
                print("Letters guessed:", ", ".join(g.missedLetters))
                print("\ng = guess, t = tell me, l for a letter, and q for quit")

                option = input("Enter option (g, t, l, or q): ").lower()

                if option in ['g', 't', 'l', 'q']:
                    match option:
                        case 'g':
                            guess = input("\nMake your guess: ").lower()
                            if guess == current_word.lower():
                                print("\n@@\n@@FEEDBACK: WoOhOo you guessed correctly!\n@@")
                                g.status.append("Success")
                                key = input("\nPress any key to play again or 'q' to exit the game....\n").lower()
                                if key == 'q':
                                    self.quit_game = True
                                quit_round = True
                                os.system('cls' if os.name == 'nt' else 'clear')

                            else:
                                print("\n@@\n@@FEEDBACK: Try again :(\n@@")
                                key = input("\nPress any key to continue...\n")
                                g.updateBadGuess()
                                os.system('cls' if os.name == 'nt' else 'clear')

                        case 't':
                            print(f"\n@@\n@@FEEDBACK: Why did you give up...'{current_word}'\n@@")
                            g.status.append("Gave Up")
                            key = input("\nPress any key to play again or 'q' to exit the game\n").lower()
                            if key == 'q':
                                self.quit_game = True
                            quit_round = True
                            os.system('cls' if os.name == 'nt' else 'clear')

                        case 'l':
                            letter = input("\nEnter a letter: ").strip().lower()
                            
                            if not letter:
                                print("\n@@\n@@FEEDBACK: No letters entered. Press any key to continue.\n@@")
                                key = input("\nPress any key to continue...\n")
                                os.system('cls' if os.name == 'nt' else 'clear')

                            elif not letter.isalpha():
                                print("\n@@\n@@FEEDBACK: Invalid letter. Please enter a valid alphabetical character.\n@@")
                                key = input("\nPress any key to continue...\n")
                                os.system('cls' if os.name == 'nt' else 'clear')

                            elif letter in set(g.correctLetters) or letter in set(g.missedLetters):
                                print(f"\n@@\n@@FEEDBACK: Letter '{letter}' has already been guessed. Guess another letter.\n@@")
                                key = input("\nPress any key to continue...\n")
                                os.system('cls' if os.name == 'nt' else 'clear')

                            elif letter in current_word.lower():
                                g.addCorrectLetters(letter.lower())

                                if set(g.correctLetters) == set(current_word.lower()):
                                    print("\n@@\n@@FEEDBACK: WoOhOo you guessed correctly!\n@@")
                                    g.status.append("Success")
                                    key = input("\nPress any key to play again or 'q' to exit the game\n").lower()
                                    if key == 'q':
                                        self.quit_game = True
                                    quit_round = True
                                    os.system('cls' if os.name == 'nt' else 'clear')

                                else:    
                                    print("\n@@\n@@FEEDBACK: WoOhOo you found one letter!\n@@")
                                    key = input("\nPress any key to continue...\n")
                                    os.system('cls' if os.name == 'nt' else 'clear')
                            else:
                                    print("\n@@\n@@FEEDBACK: Letter not found :(\n@@")
                                    key = input("\nPress any key to continue...\n")
                                    g.addMissedLetter(letter.lower())
                                    g.updateBadLetters()
                                    os.system('cls' if os.name == 'nt' else 'clear')

                        case 'q':
                            g.status.append("Gave Up")
                            quit_round = True
                            self.quit_game = True
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\nInvalid option. Please re-enter option.")
                    
            
            # Add the game played in the games_played array
            self.games_played.append(g)
            g.calculate_score()
            self.total_score += g.final_score

        # Print the report
        print("\n++")
        print("++ Game Report")
        print("++\n")
        print("Game      Word         Status      Bad Guesses      Missed Letters      Score")
        print("----      ----         ------      -----------      --------------      -----")

        for idx, g in enumerate(self.games_played):
            print(f"{idx + 1:<9} {g.word_to_guess:<12} {', '.join(g.status):<11} {g.badGuess:^14} {g.badLetters:^21} {g.final_score}")

        print(f"\nFinal Score: {round(self.total_score,2)}")

        

        
        



