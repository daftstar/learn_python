import json
data_dict = json.load(open("data_files/data.json"))


def get_definition():
    word = input("what would you like to lookup? ").lower()

    if word in data_dict:
        answer = data_dict[word]

        if len(answer) > 1:
            full_answer = '\n'.join(str(item) for item in answer)
            return full_answer
        else:
            return answer[0]

    else:
        return "%s is not in the dictionary" % word


print (get_definition())
