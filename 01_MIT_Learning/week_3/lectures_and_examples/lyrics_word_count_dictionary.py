# Program to find how many times word appears in lyrics
# 3 functions needed
#
# 1) Frequency mapping dictionary
# 2) Find words that occur most times
# 3) Find words that occur least times
import string

under_the_pressure = "Well the comedown here was easy Like the arrival of a new day But a dream like this gets wasted Without you Under the pressure is where we are You're the only one Like an illusion When it all breaks down and we're runaways Standing in the wake of our pain And we stare straight into nothing But we call it all the same You were raised on a promise Found that over time Better come around to the new way Or watch as it all breaks down here Well the break down Stole it all the way across Stranded on When you come here and I'm wasted Lying on a hill dancin' in the rain Hidin in the back loosening my grip I'm just wading in the water Just trying not to crack under the pressure pressure pressure pressure pressure"
under_the_pressure_list = under_the_pressure.split()


# remove lame words
def cleanse_lyrics(lyrics):
    ignore = ["the", "a", "it", "in", "but", "all", "on", "as"]
    new_lyrics = []

    for word in lyrics:
        if word not in ignore:
            new_lyrics.append(word.lower())
    return (new_lyrics)


# run frequency analysis on new list of words / sans lameness
def lyrics_to_frequencies(lyrics):
    lyrics_for_review = cleanse_lyrics(lyrics)

    myDict = {}         # {lyric, instance}

    for word in lyrics_for_review:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict



# display words that are shown most frequently
def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []

    for key, value in song.items():
        print (key + ": " + str(value))
        print ()

    for key in freqs:
        if freqs[key] == best:
            words.append(key)
    return (words, best)


song = (lyrics_to_frequencies(under_the_pressure_list))
(word, count) = most_common_words(song)
print (word, count)


