import pandas

# Create a dictionary in this format:
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
input_word = input("Input word: ").upper()

words = [alphabet_dict[letter] for letter in input_word]

print(words)