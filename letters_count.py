import string 
from string import digits

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("There is no such file: ", fname)
    exit

counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    word= line.split()
    for char in word:
        if char.isalpha():
            char += char
            list(char)
            for i in char:
                if i not in counts:
                    counts[i] = 1
                else:
                    counts[i] += 1
total = sum(counts.values())
print("Total letters count: ", total)

# Convert dictionary to a list and sort it by its values.
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))
lst.sort(reverse = True)

# Return the count of each letter
    
for key, val in lst:
    print (val, str(round((key/total)*100,2)) + "%")
    


