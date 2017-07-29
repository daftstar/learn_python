def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain
        N unique lowercase letters.

        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to
        str where each key is a letter in map_from at
        index i and the corresponding value is the
        letter in map_to at index i.

        Decoded is a string that contains the decoded version
        of code using the key_code mapping.

        For example:
              p_text   cipher   value
        cipher("abcd", "dcba", "dab") returns:

        ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')
    """
    # blank decoded message
    decoded = ""

    # create separate lists for each map params
    l_map_from = [p for p in map_from]
    l_map_to = [c for c in map_to]

    # create dictionary from two param lists
    crypto = dict(zip(l_map_from, l_map_to))

    # for each letter in code param,
    # find the matching key in crypto and
    # append the matching value to the decoded sting
    for i in code:
        decoded += crypto[i]

    # return tuple consisting of dictionary and encrypted message
    return (crypto, decoded)


print (cipher("abcd", "wxyz", "dab"))
