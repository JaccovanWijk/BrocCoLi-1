from langdetect import *
import os

def make_profiles(datafolder="./training", profilefolder="./trigram-models", size = 200):

    # Create the folder, if it doens't exist
    if not os.path.exists(profilefolder):
        os.makedirs(profilefolder)

    trainingFiles = os.listdir(datafolder) # List all the files in the folder

    # For all the files, write their trigrams to a new file
    for fileName in trainingFiles:
        name = fileName.split("-")
        language = name[0]
        enc = name[1]
        with open(datafolder+"/"+fileName, encoding=enc) as file :
            table = trigram_table(file.read(), size)
            write_trigrams(table,profilefolder+"/"+language+"."+str(size))

if __name__ == "__main__":
    make_profiles()

