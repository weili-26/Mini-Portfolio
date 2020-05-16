import os
import json
from difflib import get_close_matches


filepath = os.path.join(os.path.expanduser("~"), "Desktop", "data.json")
with open(filepath) as file:
    data = json.load(file)


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print('do you mean %s ?' %get_close_matches(word, data.keys())[0])
        decide = input('y for Yes and n for no')
        if(decide == 'y'):
            return data[get_close_matches(word , data.keys())[0]]
        elif(decide == 'n'):
            return 'retype'
        else:
            return 'Invalid keyword'
    else:
        return 'Invalid keyword'


x = 'y'
while(x == 'y'):
    word = input('search for a keyword')
    output = translate(word)
    if type(output) == list:
        for i in output:
            print(i)
    else:
        print(output)
