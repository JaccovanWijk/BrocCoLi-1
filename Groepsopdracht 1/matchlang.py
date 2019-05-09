from langdetect import *
import os

class LangMatcher:

    def __init__(self, path):

        # create dict
        self.frequencies = {}

        # fill dict with key language and value a dict of frequencies
        for filename in os.listdir(path):
            language = filename[:filename.index(".")]
            data = read_trigrams(path + "/" + filename)
            self.frequencies[language] = data

    def score(self, text, n=1, ngrams=200):

        # ask for the ngram table
        table = trigram_table(text, ngrams)

        # calculate scores and make dict with languages and scores
        scores = {}
        for language in self.frequencies:
            scores[language] = cosine_similarity(table, self.frequencies[language])

        return dict(sorted(scores.items(), key=operator.itemgetter(1), reverse=True)[:n])

    def recognize(self, filename, encoding="utf-8", ngrams=200):

        with open(filename, encoding=encoding) as file:
            return self.score(file.read(), ngrams=ngrams)

app = LangMatcher("./trigram-models")
print(app.recognize("austen-emma.txt"))

