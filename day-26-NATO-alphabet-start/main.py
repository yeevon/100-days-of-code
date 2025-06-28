import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for index, row in df.iterrows()}
print(phonetic_dict)

def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        print([phonetic_dict[letter] for letter in user_input])
    except KeyError:
        print('Sorry, only letters in the alphabet please.')
        generate_phonetic()

generate_phonetic()


