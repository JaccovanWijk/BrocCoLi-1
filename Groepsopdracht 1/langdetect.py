import re
import collections

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
    tokens = sorted(tokens.items(), key=lambda kv: kv[1])
    return collections.OrderedDict(tokens)[:limit]

def read_table():
    """Read table:)"""
    print(2)

def write_table():
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
