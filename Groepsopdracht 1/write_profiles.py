from langdetect import *

if __name__ == "__main__" :
    main()

def __main__(self,args):
    make_profiles()

def make_profiles(datafolder="./training", profilefolder="./trigram-models", size = 200):

    # Create the folder
    if not os.path.exists(folder):
        os.makedirs(folder)

    trainingFiles = os.listdir(datafolder) # List all the files in the folder
    for fileName in trainingFiles:
        name = fileName.split("-")
        language = name[0]
        encoding = name[1]
        with open(fileName, encoding=encoding) as file :
            table = trigram_table(fileName.read(), size)
            write_trigrams(table,language+"."+str(size))


