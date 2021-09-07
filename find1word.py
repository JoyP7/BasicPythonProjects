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

# Return the count of the requested word
tmp = input("What word you want to find? ")
print("Count of " + tmp + ":",counts.get(tmp))