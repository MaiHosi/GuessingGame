#maintain information about a specific game
#keeps track of words guess and letters
class Game:
    
    word_to_guess = None

    def __init__(self, word_to_guess):
        self.word_to_guess = word_to_guess
        self.correctLetters = set()
        self.missedLetters = set()
        self.status = []
        self.badGuess = 0
        self.badLetters = 0
        self.final_score = 0


    def updateBadGuess(self):
        self.badGuess += 1

    def updateBadLetters(self):
        self.badLetters +=1

    def addMissedLetter(self, missedLetters):
        self.missedLetters.add(missedLetters)
    
    def addCorrectLetters(self, letter):
        self.correctLetters.add(letter)
    
    def calculate_score(self):
        letter_frequencies = {
            'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70,
            'f': 2.23, 'g': 2.02, 'h': 6.09, 'i': 6.97, 'j': 0.15,
            'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51,
            'p': 1.93, 'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06,
            'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97,
            'z': 0.07
        }

        points = 0
        final_score = 0

        # If the player gave up without guessing any letters or guessed only bad letters
        if not self.correctLetters and not self.badGuess and 'Gave Up' in self.status:
            # Subtract the frequencies of all letters in the word
            points -= sum(letter_frequencies.get(letter, 0) for letter in set(self.word_to_guess.lower()))
            final_score = points 

        #if the player guesses the word directly
        if not self.correctLetters and not self.badGuess and 'Success' in self.status:
            points += sum(letter_frequencies.get(letter, 0) for letter in set(self.word_to_guess.lower()))
            final_score = points 
            
        # If the player guessed some letters and gave up
        elif set(self.correctLetters) != set(self.word_to_guess) and 'Gave Up' in self.status:
            blank_letters = set(self.word_to_guess.lower()) - set(self.correctLetters)
            points -= sum(letter_frequencies.get(letter, 0) for letter in blank_letters)

            # Penalty for incorrect guesses
            penalty = 0.1 * abs(points) * self.badGuess
            final_score = points - penalty
            
        # If they guessed all the correct letters and it's a success
        elif set(self.correctLetters) == set(self.word_to_guess) and 'Success' in self.status:
            points += sum(letter_frequencies.get(letter, 0) for letter in self.word_to_guess)
            final_score = points
                
        # If they guessed a few letters and guessed correctly the word
        elif set(self.correctLetters) != set(self.word_to_guess) and 'Success' in self.status:
            blank_letters = set(self.word_to_guess.lower()) - set(self.correctLetters)
            points += sum(letter_frequencies.get(letter, 0) for letter in blank_letters)

            # Divide by the number of bad letters
            if self.badLetters >= 1:
                score = points / self.badLetters
            else:
                score = points
                
            # Penalty for incorrect guesses
            penalty = 0.1 * abs(points) * self.badGuess
            final_score = score - penalty
                
        self.final_score = round(final_score, 2)

