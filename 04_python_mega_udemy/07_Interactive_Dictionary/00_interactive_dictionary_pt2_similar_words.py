import json
from difflib import get_close_matches


def get_definition():
    """Requires no inputs
    data_dict is dictionary of lots of words and definitions
    asks users for a word, returns value (or guessed value if word
    isn't found.)
    """

    data_dict = json.load(open("data_files/data.json"))
    word = input("what would you like to lookup? ").lower()
    # word = "rain"
    # word = "rainn"
    # word = "kjsdjkhsdkfljsdkl"

    # TO DO - clean up redundant code!
    if word in data_dict:
        answer = data_dict[word]

        # check if returned answer has multiple definitions
        if len(answer) > 1:
            full_answer = '\n'.join(str(item) for item in answer)
            return full_answer
        else:
            return answer[0]

    # word cannot be found, so move to fuzzy search
    else:
        # return "%s is not in the dictionary" % word
        if get_close_matches(word, data_dict.keys()) == []:
            return "Sorry, no idea what you're talking about"

        else:
            closest_match = get_close_matches(word, data_dict.keys())[0]

            print ("looks like you meant to search for: " + closest_match + "\n")
            answer = data_dict[closest_match]

            # check if returned answer has multiple definitions
            if len(answer) > 1:
                full_answer = '\n'.join(str(item) for item in answer)
                return full_answer
            else:
                return answer[0]


print (get_definition())
