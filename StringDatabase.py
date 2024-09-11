import random

def read_words(fileName):
    with open(fileName, 'r') as file:
        lines = file.readlines()
        words_list = [line.split() for line in lines]
        words = [word.strip() for sublist in words_list for word in sublist]

    return words
