import json
from difflib import get_close_matches

data = json.load(open('dic.json'))

def retrive_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        for i in range(len(get_close_matches(word, data.keys()))):
            action = input("Did you mean {} instead? ['y' or 'n']".format(get_close_matches(word, data.keys())[i]))
            if action == 'y':
                return data[get_close_matches(word, data.keys())[i]]
            elif action == 'n':
                if i < len(get_close_matches(word, data.keys())):
                    continue
                elif i == len(get_close_matches(word, data.keys())):
                    return ('The word does not exist, yet.')
    else:
        return ("We don't understand your entry. Apologies.")
    return ("The word doesn’t exist, please double check it.")

if __name__ == '__main__':
    print('Wellcome to Interactive Dictionary!')
    while True:
        word_user = input('Enter a word or "q" for exit: ')
        if word_user == 'q':
            print('Bye!!!')
            exit(0)
        output = retrive_definition(word_user)
        if type(output) == list:
            [print('- ', item) for item in output]
        else:
            print('- ', output)