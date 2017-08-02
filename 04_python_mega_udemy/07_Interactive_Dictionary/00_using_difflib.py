import json
from difflib import SequenceMatcher
from difflib import get_close_matches
data_dict = json.load(open("data_files/data.json"))


ratio = SequenceMatcher(None, "rainn", "rain").ratio()
print (ratio)

print (get_close_matches("rainn", ["help", "pyramid", "rain"]))

# using json data
# print (get_close_matches("rainn", data_dict.keys(), n=10, cutoff=0.8))
# print (get_close_matches("rainn", data_dict.keys(), n=3, cutoff=0.8))
# print (get_close_matches("rainn", data_dict.keys()))

# first item in list is highest match
closest_match = get_close_matches("rainn", data_dict.keys())[0]
print (closest_match)
