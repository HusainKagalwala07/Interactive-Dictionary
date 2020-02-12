#importing JSON library

import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches


#data is a type of dictionary, which helps to load the data from JSON file

data = json.load(open("data.json"))

#Function to return the meaning of the word that user Enter

def translation(word):

    #Converting the word into lower-case
    word = word.lower()

    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        yn = input("Did you mean %s instead ? If Yes then Press Y else Press N.." %get_close_matches(word,data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(word,data.keys())[0]]
        elif word.title() in data:
            return data[word.title()]
        elif word.upper() in data:
            return data[word.upper()]
        elif yn == 'N':
            return "Sorry!!! Your Given Word Does'nt Exist..."
        else:
            return "We were not able to understand the query..."
    else:
        return "Sorry!!! Your Given Word Does'nt Exist.."


#Input from user

word = input("Enter the word whose meaning is to be found out :")

#Printing the meaning of the word

output = translation(word)

if type(output) == list:
    for items in output:
        print(items)
else:
    print(output)
