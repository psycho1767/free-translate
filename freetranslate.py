import requests 
import time


inp = ''
while inp != 'exit':
    inp1 = input('enter farsi language : ')
    data = requests.get(f'https://zarebin.ir/we/api/v1/translate?originLanguage=FA&destinationLanguage=EN&translationSource=GOOGLE&query={inp}&qsrc=user')
    ld = dict(data.json())
    print(ld['answer'])
    inp = inp1