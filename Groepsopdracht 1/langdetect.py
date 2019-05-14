import re
import operator
import math


def trigram_table(text, limit=0):
    """Calculate trigram frequency table from string and return it"""
    newstring = prepare(text)

    # Give every word a < and >
    for i, word in enumerate(newstring):
        newstring[i] = '<' + word + '>'

    # Make dict and count all tokens
    tokens = dict()
    for word in newstring:
        trigram = trigrams(word)
        for gram in trigram:
            if gram not in tokens:
                tokens[gram] = 1
            else:
                tokens[gram] += 1

    # If the limit is 0, return everything
    if limit == 0 :
        return dict(sorted(tokens.items(), key=operator.itemgetter(1), reverse=True))
    # Else, return the list upto the limit
    else :
        return dict(sorted(tokens.items(), key=operator.itemgetter(1), reverse=True)[:limit])


def read_trigrams(filename):
    """Read a file containing the trigrams scores and return them as a dictionary"""
    with open(filename, encoding="utf-8") as file:
        alltext = file.readlines()
        tuples = dict()
        for line in alltext:
            tuple = line.split()
            tuples[tuple[1]] = int(tuple[0])
        return tuples


def write_trigrams(table, filename):
    """"Write a trigram table to the specified file"""
    with open(filename, 'w', encoding="utf-8") as file:
        for line in table.items():
            file.write(str(line[1]) + " " + line[0] + "\n")


def cosine_similarity(known, unknown):
    """Return cosine-similarity between two frequency tables"""
    dotproduct = 0
    for key in known.keys():
        if key in unknown.keys():
            dotproduct += known[key] * unknown[key]
    magnitudes = math.sqrt(sum([x*x for x in known.values()])) * math.sqrt(sum([x*x for x in unknown.values()]))
    return dotproduct / magnitudes


def prepare(text):
    """Takes in a string.
    Replaces the following characters with spaces: !?",.()<>
    Splits the new string on whitespace and returns that list."""

    text = re.sub(r"[!? .,\"<>()]"," ",text)
    newstring = text.split()
    return newstring


def trigrams(seq):
    """Takes in any sequence (i.e. list or string).
    Return a list of its trigrams"""
    trigram = []
    length = len(seq)
    for i in range(length):
        if length > i + 2:
            trigram.append(seq[i:i+3])
    return trigram
