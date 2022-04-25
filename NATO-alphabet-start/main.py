import pandas
data_info = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data_info.iterrows()}
user_input = input("Enter a word: ").upper()
phonetic_answer = [phonetic_dict[letter] for letter in user_input]
print(phonetic_answer)
