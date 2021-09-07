import string
# Input the file
fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("There is no such file:", fname)
    exit

# Count every single words in the file
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for i in words:
        if i not in counts:
            counts[i] = 1
        else:
            counts[i] += 1

#Total words  
total = sum(counts.values())
print("Total words: ", total)

# Convert dictionary to a list and sort it by its values.
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))
lst.sort(reverse = True)

# Return the top 10 common words
for key, val in lst[:10]:
    print (val, key)
        
