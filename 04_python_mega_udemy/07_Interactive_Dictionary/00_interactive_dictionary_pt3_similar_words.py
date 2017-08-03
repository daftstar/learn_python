import json
from difflib import get_close_matches


def get_definition():
    """Requires no inputs
    data_dict is dictionary of lots of words and definitions
    asks users for a word, returns value (or guessed value if word
    isn't found.)
    """
    # This is ineffiecient, as we're loading the entire datafile
    # into memory. TODO: Use database insted of entire file load ;)
    data_dict = json.load(open("data_files/data.json"))

    word = input("what would you like to lookup? ").lower()
    # word = "rainn"
    # word = "rain"
    # word = "kjshdfiushiuf"

    # ---------------- HELPER FUNCTIONS ----------------
    def valid_word_check(word):
        """Helper function to determine if user input is valid.
            Input is word - variable defined by user input
            Returns True / False"""
        if word in data_dict:
            return True
        else:
            return False

    def word_definition_parser(answer):
        """Helper function that parses out multiple definitions of a word
            Input: answer - list variable defined by presence of word in data_dict
            Returns parsed answer or single answer depending on list length"""
        # check if returned answer has multiple definitions
        if len(answer) > 1:
            full_answer = '\n'.join(str("-" + item) for item in answer)
            return full_answer
        # otherwise, list returns with only 1 value, return that first value
        else:
            return answer[0]

    # ------------- END OF HELPER FUNCTIONS ----------------

    # ------------- CORE FUNCTION LOGIC --------------------
    # Check user input for word validity
    if valid_word_check(word):
        answer = data_dict[word]
        return (word_definition_parser(answer))

    # Else, word cannot be found, so move to fuzzy search
    else:
        # Check if there's a close word match to user's input
        # Base case, there is a close match
        if len(get_close_matches(word, data_dict.keys())) > 0:
            # First list value will be highest probability match
            closest_match = get_close_matches(word, data_dict.keys())[0]

            print ("looks like you meant to search for: " + closest_match + "\n")
            answer = data_dict[closest_match]
            return (word_definition_parser(answer))
        else:
            # base case was not met, and we assume user entered gibberish
            return "Sorry, I can't find a word close to: " + word


print (get_definition())
