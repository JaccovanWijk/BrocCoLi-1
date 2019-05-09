import re
import operator

def trigram_table(string, limit):
    """Calculate trigram frequency table  from string and return it"""
    newstring = prepare(string)

    # Give every word a < and >
    for i, word in enumerate(newstring):
        newstring[i] = '<' + word + '>'

    # Make dict and count all tokens
    tokens = {}
    for word in newstring:
        trigram = trigrams(word)
        for gram in trigram:
            if gram not in tokens:
                tokens[gram] = 1
            else:
                tokens[gram] += 1
    if limit < 1 :
        return dict(sorted(tokens.items(), key=operator.itemgetter(1), reverse=True))
    else :
        return dict(sorted(tokens.items(), key=operator.itemgetter(1), reverse=True)[:limit])

def read_table(filename):
    """Read a file containing the trigrams scores and return them as a dictionary"""
    with open(filename, encoding="utf-8") as file:
        alltext = file.readlines();
        tuples = dict()
        for line in alltext:
            tuple = line.split();
            tuples[tuple[1]] = int(tuple[0])
        return tuples

def write_table(table, filename):
    """"Write"""
    print(3)

def cosine_similarity(table1, table2):
    """Return cosine between two frequency tables"""
    print(4)

def prepare(string):
    string = re.sub(r"[!? .,\"<>()]"," ",string)
    newstring = string.split()
    return newstring

def trigrams(string):
    trigram = []
    length = len(string)
    for i in range(length):
        if length > i + 2:
            trigram.append(string[i:i+3])
    return trigram
