import re

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

    return tokens

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
    # Delete last character if it's a wrong one (to help the split function)
    characters = ['!','?',',','.','"','(',')','<','>']
    if string[-1] in characters:
        string = string[:-1]
    if string[0] in characters:
        string = string[1:]

    newstring = re.split('[!/?,.()<>" ]+', string)  #DEZE NEEMT DE ! AAN T EINDE VAN DE ZIN ALS LEEG WOORD
    return newstring

def trigrams(string):
    trigram = []
    length = len(string)
    for i in range(length):
        if length > i + 2:
            trigram.append(string[i:i+3])
    return trigram
