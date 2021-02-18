import pandas

# Create a dictionary in this format:
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
input_word = input("Input word: ").upper()

words = []
for letter in input_word:
    try:
        words.append(alphabet_dict[letter])
    except KeyError:
        print("You are only allowed to input letters.")

print(words)