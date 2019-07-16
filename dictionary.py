import json
from difflib import get_close_matches

with open('data.json') as file:
    data = json.load(file)


choice = 'Y'

while choice is 'Y':
    try:
        key = (input('Enter a word to get it\'s definition: ')).lower()
        key = get_close_matches(key, data.keys(), n=1, cutoff=0.6)
        count = 1
        for value in data[key[0]]:
            print(f'{count}. {value}')
            count += 1
        choice = input('Do you want to continue ? (Y/N) ')
    except IndexError:
        print('Choose another word')
        continue
