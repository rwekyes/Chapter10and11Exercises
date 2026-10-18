# 10.11.1 Ask A Virtual Assistant
# In this chapter, I said the keys in a dictionary have to be hashable and I gave a short explanation.
# If you would like more details, ask a virtual assistant, “Why do keys in Python dictionaries have to be hashable?”
#
# In a previous section, we stored a list of words as keys in a dictionary so that we could use an
# efficient version of the in operator. We could have done the same thing using a set, which is another
# built-in data type. Ask a virtual assistant, “How do I make a Python set from a list of strings and check
# whether a string is an element of the set?”

# Claude Opus 5.5 said this:

#
# Sonnet I: Why do keys in Python dictionaries have to be hashable?
#
#   When thou wouldst store a value by its key,
#   The dictionary hashes it to find
#   A numbered slot where that pair's meant to be,
#   Then leaps there straight, and leaves the rest behind.
#   But should that key be changed once it is stored,
#   Its hash would shift and point some other way;
#   The dict would seek it where it ne'er was moored,
#   And thy lost value fade from light of day.
#   Thus lists, which may be altered at a whim,
#   Raise TypeError when made a key by thee,
#   While strings and ints, and tuples firm of limb,
#   Hold fast their hash through all eternity.
#     So equal keys must equal hashes bear,
#     And never change, else none shall find them there.
#
# Sonnet II: How do I make a Python set from a list of strings and check
# whether a string is an element of the set?
#
#   Take thou thy list of strings, and pass it in
#   To set(), which builds a set from what it's fed;
#   All duplicates it casts away like sin,
#   And keeps but one of each, the rest struck dead.
#   Write s = set(words): the deed is done;
#   Then ask if "pear" in s, and swift as light
#   Comes True or False, no need to search each one,
#   For hashing leaps straight to the place aright.
#   A list, by contrast, trudges word by word,
#   And slower grows as longer grows the line;
#   The dict-of-keys trick thou hast lately heard
#   Doth work as well, but sets read clean and fine.
#     Mark: {} makes a dict. For sets, write set(),
#     And so thy empty set thou shalt beget.

# 10.11.2 Exercise

def value_counts(string):
    counter = {}
    for letter in string:
        counter[letter] = counter.get(letter, 0) + 1
    return counter

# 10.11.3 Exercise

def has_duplicates(word):
    if sorted(value_counts(word).items())[-1][1] > 1:
        return True
    return False

#print(has_duplicates("bannana"))
#print(has_duplicates("dog"))

# 10.11.4 Exercise

def find_repeats(counter):
    result = {}
    for key in counter:
        if counter[key] > 1:
            result[key] = counter[key]
    return result

#print(find_repeats(value_counts("bannana")))

# 10.11.5 Exercise

from collections import Counter # the + operator didn't work, so I figured out someone else already made it work

def add_counters(counter1, counter2):
    return Counter(counter1) + Counter(counter2)

#print(add_counters(value_counts("bannana"), value_counts("bannanas")))

# 10.11.6 Exercise

with open('words.txt') as f:
    word_list = {line.strip(): 1 for line in f}

def is_interlocking(word):
    if word[0::2] in word_list and word[1::2] in word_list:
        return True
    return False

#print(is_interlocking("schooled"))
#print(is_interlocking("prestidigitation"))

for word in word_list:
    if len(word) >= 8 and is_interlocking(word):
        first = word[0::2]
        second = word[1::2]
        print(word, first, second)