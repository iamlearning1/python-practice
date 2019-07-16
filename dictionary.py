import json

with open('data.json') as file:
    data = json.load(file)


choice = 'Y'

while choice is 'Y':
    try:
        key = (input('Enter a word to get it\'s definition: ')).lower()
        count = 1
        for value in data[key]:
            print(f'{count}. {value}')
            count += 1
        choice = input('Do you want to continue ? (Y/N) ')
    except KeyError:
        print('Choose another word')
        continue
