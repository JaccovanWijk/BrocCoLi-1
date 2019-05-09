from langdetect1 import *
import os


def make_profiles(datafolder="./training", profilefolder="./trigram-models", size = 200):

    # Create the folder
    if not os.path.exists(profilefolder):
        os.makedirs(profilefolder)

    trainingFiles = os.listdir(datafolder) # List all the files in the folder
    for fileName in trainingFiles:
        name = fileName.split("-")
        language = name[0]
        enc = name[1]
        print("We gaan nu proberen iets te doen")
        with open(fileName, encoding=enc) as file :
            table = trigram_table(fileName.read(), size)
            write_trigrams(table,language+"."+str(size))

if __name__ == "__write_profiles__" :
    print("Hallo")
    make_profiles()
