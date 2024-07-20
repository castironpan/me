import requests
import json

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

file_path = r"..\me\set4\Trispokedovetiles(laser).gcode"

with open(file_path, 'r') as g_code:
    g_code_lines = g_code.readlines()

lasers = 0

for line in g_code_lines:
    if "M10 P1" in line:
        lasers += 1

print(lasers)

g_code.close()