import os
import sys
import matchlang as ml


def eval(path, lm=None, trigrammodels="./trigram-models", ngrams=200, rounding=4):
    """This function prints the evaluation of the files in the path specified, when matched with a language"""

    print("We are now going to evaluate the files in the specified path " + path)

    # Create the initial language dictionary and fill it
    languages = dict()
    languages["da"] = "Danish"
    languages["de"] = "German"
    languages["el"] = "Greek"
    languages["en"] = "English"
    languages["es"] = "Spanish"
    languages["fi"] = "Finnish"
    languages["fr"] = "French"
    languages["it"] = "Italian"
    languages["nl"] = "Dutch"
    languages["pt"] = "Portuguese"
    languages["sv"] = "Swedish"

    path = "./test-clean/" + path  # Correct the default path
    filepaths = os.listdir(path)  # List all the actual file paths

    # Create a LangMatcher element if it does not exist yet, otherwise, reuse the current one
    # NOTE : This is just to be sure. Normally you would always provide a LangMatcher when calling this function
    if lm is None:
        langmatcher = ml.LangMatcher(trigrammodels)
    else:
        langmatcher = lm

    correct = 0
    incorrect = 0

    # Iterate trough all files and score them
    for filepath in filepaths:
        with open(path + "/" + filepath, encoding="utf-8") as file:
            text = file.read()
            score = langmatcher.score(text, ngrams=ngrams).popitem()  # Guess which language it is
            actuallanguage = languages[filepath[-2:]]  # The actual language, defined by the file extension
            message = ""  # Set a default empty error message

            if not score[0] == actuallanguage:
                message = "- ERROR : The correct language was " + actuallanguage
                incorrect += 1
            else:
                correct += 1

            print(filepath, "-", score[0], "with a score of", round(score[1], rounding), message)

    print("Correct :", correct, "/", correct+incorrect, ". Incorrect :", incorrect, "/", correct+incorrect)
    print()


def main():

    lm = ml.LangMatcher("./trigram-models") # Create a langmatcher to use for every
    eval("europarl-90", lm=lm)
    eval("europarl-30", lm=lm)
    eval("europarl-10", lm=lm)

if __name__ == "__main__":
    main()
