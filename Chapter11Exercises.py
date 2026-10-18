# 11.11.2 Exercise

list0 = [1, 2, 3]
list1 = [4, 5]

t = (list0, list1)
print(t)

list1.append(6)

#d = {t: 'this tuple contains two lists'}
# Type Error to the max, PyCharm even flagged it before I ran it

# Asked Claude Opus 5.5 - 'Are Python tuples always hashable?'

#  1. The box. The mime pulls an invisible box out of the air and presses on each wall, then shoves it
#     hard with a shoulder. Nothing moves. They try to pry the lid open and can't. A tuple is immutable.
#  2. The happy case. The mime drops three heavy stones into the box and pushes it through a stamping
#     machine. A ticket comes out (the hash). They slide the box into a numbered cubbyhole in the wall
#     and bow. A tuple of ints or strings works as a dictionary key.
#  3. The stretchy bags. The mime builds a second box just as solid, but puts two floppy, stretchy bags
#     inside instead of stones. These are the lists [1, 2, 3] and [4, 5].
#  4. Reaching inside. The mime reaches in, stretches the second bag open, and stuffs in one more item.
#     They step back and point at the box, still the same shape. Then they point at the bag, which is
#     now bigger, and look at the audience with wide eyes. t[1].append(6) works: the tuple didn't change,
#     but what's inside it did.
#  5. The jam. The mime feeds the second box into the stamping machine. It grinds and sputters, then gets
#     stuck on the bag. The mime gets a shock and staggers back with their hair standing up. Then they
#     hold up an invisible sign: TypeError: unhashable type: 'list'.
#  6. The fix. The mime swaps each floppy bag for a rigid tube, raps one on the floor to show it's solid,
#     and sends the box through again. A ticket comes out and the box slides into a cubbyhole. Converting
#     the lists to tuples makes the whole thing hashable.
#  7. The moral. The mime faces the audience and wobbles a flat hand side to side: "not always." Then they
#     hold up one finger: "only if everything inside is hashable too." They bow.

# 11.11.3 Exercise

letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range(len(letters))
letter_map = dict(zip(letters, numbers))

def shift_word(word, n):
    result = []
    for letter in word:
        result.append(
            letters[(letter_map[letter] + n) % 26]
        )
    return "".join(result)

print(shift_word("cheer",7))
print(shift_word("melon",16))

# 11.11.4 Exercise

from Chapter10Exercises import value_counts

def second_element(t):
    return t[1]

def most_frequent_letters(word):
    print(sorted(value_counts(word).items(), key=second_element, reverse=True))

most_frequent_letters("bannana")

# 11.11.5 Exercise

with open('words.txt') as f:
    word_list = {line.strip(): 1 for line in f}

def anagram_dict():
    anagrams = {}
    for word in word_list:
        sort_word = "".join(sorted(word.strip()))
        anagrams_for_word = anagrams.get(sort_word, [])
        anagrams_for_word.append(word.strip())
        anagrams[sort_word] = anagrams_for_word
    return anagrams

def print_anagrams(test_words):
    anagrams = anagram_dict()
    for word in test_words:
        sort_word = "".join(sorted(word.strip()))
        print(f"{anagrams[sort_word]}")

print_anagrams(['deltas', 'retainers', 'generating', 'termless'])

# 11.11.6 Exercise

def word_distance(word1, word2):
    if len(word1) != len(word2):
        return 0
    count = 0
    for pair in zip(list(word1), list(word2)):
        if pair[0] != pair[1]:
            count += 1
    return count

#print(word_distance("beer", "deer"))
#print(word_distance("cat", "dog"))
#print(word_distance("wrong", "word"))

# 11.11.7 Exercise

def metathesis():
    anagrams = anagram_dict()
    for sorted_word, n in anagrams.items():
        if len(n) > 1:
            for i in range(len(n)):
                for j in range(i + 1, len(n)):
                    if word_distance(n[i], n[j]) == 2:
                        print(f"{n[i]} : {n[j]}")

metathesis()