#parses the command line parameter and starts the guessing game
from Guess import Guess
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python words.py [play | test]")
    else:
        mode = sys.argv[1].lower()
        if mode not in ['play', 'test']:
            print("Invalid mode. Please choose 'play' or 'test'.")
        else:
            game = Guess(mode)
            game.start_game()