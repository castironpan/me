import requests
import json
import random

# def be_silly(top_part, bottom_part):
#     try:
#         return top_part / bottom_part
#     except TypeError as my_error:
#         print(f"you are so silly! {my_error}")
#     except ZeroDivisionError as my_error:
#         print(
#             f"you are so silly! Can't divide {top_part} by {bottom_part} "
#             f"or we get infinity\n{my_error}"
#         )
#     except Exception as general_error:
#         print(general_error)


# print("10,2: ")
# print(be_silly(10, 2))
# print("Cake, 2:")
# print(be_silly("cake", 2))
# print("10 , 0: ")
# be_silly(10, 0)

# pokeList = []

# for id in range(1, 5):
#     url = f"https://pokeapi.co/api/v2/pokemon/{id}"
#     req = requests.get(url)
#     the_json = json.loads(req.text)
#     name = the_json["forms"][0]["name"]
#     height = the_json["height"]
#     weight = the_json["weight"]

#     pokemonDetails = {"name": name, "height": height, "weight": weight}
#     pokeList.append(pokemonDetails)

# orderedPokeList = sorted(int(pokeList.items()), key = lambda x:x[1]) 

# print(orderedPokeList)

# print(name)
# print(height)
# print(weight)

# file_path = r"..\me\set4\Trispokedovetiles(laser).gcode"

# with open(file_path, 'r') as g_code:
#     g_code_lines = g_code.readlines()

# lasers = 0

# for line in g_code_lines:
#     if "M10 P1" in line:
#         lasers += 1

# print(lasers)

# g_code.close()

# fizz_buzz_list = []
    
# for i in range(1,100):
#     if (i % 3 == 0) & (i % 5 == 0): 
#         fizz_buzz_list.append("FizzBuzz")
#     elif i % 3 == 0:
#         fizz_buzz_list.append("Fizz")
#     elif i % 5 == 0: 
#         fizz_buzz_list.append("Buzz")
#     else:
#         fizz_buzz_list.append(i)


# print(fizz_buzz_list)


# wd = {}

# url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength="

# for i in range(3, 7):
#     j = 0
#     wordList = []
#     while j < i:
#         randomWordGen = requests.get(url + str(i))
#         wordList.append(randomWordGen.text)
#         j += 1
#     print(wordList)
#     wd[i] = wordList

# print(wd)

def make_filler_text_dictionary():
    """Make a dictionary of random words filler text.
    There is a random word generator here:
    https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=4
    If we set wordlength=18, we will get something like this:
    >>> url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength=18"
    >>> r = requests.get(url)
    >>> r.text # will get you a string, something like this:
    >>> "occipitosphenoidal"

    Return a dictionary where the keys are numbers, and the values are lists of
    words. e.g.
    {
        3: ['Seb', 'the', 'yob', "boy"],
        4: ['aaaa', 'bbbb', 'cccc', "ddd"],
        ...
        7: ['aaaaaaa', 'bbbbbbb', 'ccccccc', 'ddddddd']
    }
    Use the API to get the 4 words.

    The dictionary should have the numbers between 3 and 7 inclusive.
    (i.e. 3, 4, 5, 6, 7 and 4 words for each)
    TIP: you'll need the requests library
    """

    import requests

    wd = {}

    url = "https://us-central1-waldenpondpress.cloudfunctions.net/give_me_a_word?wordlength="

    for i in range(3, 8):
        j = 0
        wordList = []
        while j < 4:
            randomWordGen = requests.get(url + str(i))
            wordList.append(randomWordGen.text)
            j += 1
        wd[i] = wordList

    return wd

"""Makes filler text, but really fast.

This time, the first time the code runs, save the dictionary returned
from make_filler_text_dictionary to a file.
On the second run, if the file already exists use it instead of going to
the internet.
Use the filename "dict_cache.json"
TIP: you'll need the os and json libraries
TIP: you'll probably want to use json dumps and loads to get the
dictionary into and out of the file. Be careful when you read it back in,
it'll convert integer keys to strings.
If you get this one to work, you are a Very Good Programmer™!
"""

import os
import os.path
import json

# my_dict into a file? 
# if it doesn't ald exist, use internet
#  oop 

fname = "dict_cache.json"
path = r"C:\Users\casmi\1161\me\set8\\" + fname

if os.path.isfile(path) == False:
    wall_of_text = json.dumps(make_filler_text_dictionary())
    dict_file = open(path, "w")
    dict_file.write(wall_of_text)
    dict_file.close()

json_dict_file = open(path).read()

dict_file_data = json.loads(json_dict_file)

print(dict_file_data['3'][0])

words = []

i = 0
while (i < 200):
    random_key = random.randint(3,7)
    random_index = random.randint(0,3)
    key = str(random_key)
    words.append(dict_file_data[key][random_index])
    i += 1

print(i)

print(words)
