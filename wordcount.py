import string
fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("There is no such file:", fname)
    exit
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
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))
lst.sort(reverse = True)

for key, val in lst[:10]:
    print (val, key)
        
