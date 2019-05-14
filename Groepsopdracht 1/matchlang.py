from langdetect import *
import os
import sys


class LangMatcher:
    """A class that can guess the language of a specified file based on trigram data"""

    def __init__(self, path):

        # create dict
        self.frequencies = {}

        # fill dict with key language and value a dict of frequencies
        for filename in os.listdir(path):
            language = filename[:filename.index(".")]
            data = read_trigrams(path + "/" + filename)
            self.frequencies[language] = data

    def score(self, text, n=1, ngrams=200):
        """"This function returns the score of the n best matching languages."""

        # ask for the ngram table
        table = trigram_table(text, ngrams)

        # calculate scores and make dict with languages and scores
        scores = {}
        for language in self.frequencies:
            scores[language] = cosine_similarity(table, self.frequencies[language])

        return dict(sorted(scores.items(), key=operator.itemgetter(1), reverse=True)[:n])

    def recognize(self, filename, encoding="utf-8", ngrams=200):
        """Opens a file and returns the language(s) with the highest score(s)"""
        with open(filename, encoding=encoding) as file:
            return self.score(file.read(), ngrams=ngrams)


def main():
    """When run as the main program, this script will read all the files in the commandline arguments.
    Then, it will try to guess the language of aforementioned files. It prints its guesses incl. scores"""

    args = sys.argv[1:]  # Get the commandline arguments
    enc = "utf-8"  # Set the default encoding to utf-8

    # Set a different encoding when needed
    if "-e" in args:
        i = args.index("-e")

        # Catch the error that the specified encoding can be empty
        if len(args) <= i+1:
            print("You specified an empty / no encoding. We will use utf-8 instead if that's okay with you.")
        elif args[i+1].strip() == "" or args[i+1] is None:
            print("You specified an empty / no encoding. We will use utf-8 instead if that's okay with you.")
            args.remove(enc)
        else:
            enc = args[i + 1]
            args.remove(enc)

        args.remove("-e")

    lm = LangMatcher("./trigram-models")  # Create a LangMatcher element

    # Go trough all paths in args and score them
    for filepath in args:
        with open(filepath, encoding=enc) as file:
            text = file.read()
            scores = lm.score(text)
            score = scores.popitem()
            print("We think the language of file", file.name, "is", score[0], "with a score of", round(score[1], 4))


if __name__ == "__main__":
    main()


