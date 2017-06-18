# Function to determine if a string is a palindrome

alphabet = "abcdefghijklmnopqrstuvwxyz"

def is_palindrome(string):
    """
    Recursively see if first and last characters are == to each other
    """

    # lowercase the string
    def normalize_string(string):
        string = string.lower()
        ans = ''
        
        for c in string:
            if c in alphabet:
                ans += c
        return ans  # ans will be used as 'string' in is_pal()

    def is_pal(ans):
        if len(ans) <= 1:
            return True
        else:
            return ans[0] == ans[-1] and is_pal(ans[1:-1])

    return is_pal(normalize_string(string))


print (is_palindrome("lolly"))
print (is_palindrome("b. _____&&#&#@*_______.   ob"))
