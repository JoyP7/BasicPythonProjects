import re
# Give the application some input
words = input ("Give me some words: ")

# Pattern to search for vowel
pattern = '[aeiou]'

# The nonsence app
temp = []
def nonsenseWords (words):
    test = words.split()
    for factor in test:
        x = re.match(pattern, factor[0])
        if x :
            new_words = "Z{}".format(factor)
        else:
            new_words = "{}z".format(factor)
        temp.append(new_words)
        result = " ".join(temp)
    print (result)
    
nonsenseWords(words)

