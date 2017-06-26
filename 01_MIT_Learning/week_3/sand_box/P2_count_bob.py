s = "oobbobbybobbobaodnbbobobtoboob"
search_word = "bob"
word_count = 0
start = 0

for i in range(len(s)):
    if search_word in s[start:start+len(search_word)]:
        word_count += 1
    start += 1

print ("Number of times 'bob' occurs is:",word_count)

