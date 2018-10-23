from stringManip import *
from practical_4_part1 import sampleText
from os import system

def getFileContents(filename):
    # Stuff here
    print()


def printStats(strInput, wordLength):
    # Generate a dictionary of word frequency
    wordFreqDict = getWordFrequency(strInput)
    # Generate a list of all the words in the text
    words = strInput.split()
    # Calculate the average word length
    totalWords = len(words)
    totalLetters = 0
    wordsLengthN = 0
    for word in words:
        totalLetters += len(word)
        if len(word) == n:
            wordsLengthN += 1
    avgLen = totalLetters / totalWords
    print("There are " + totalWords + " words in the input, with an average length of " + avgLen + ".")
    print("There are " + wordsLengthN + " of your selected length " + wordLength + ".")
    print("What number of the top words do you want to see?")
    topWords = int(input(">"))
    system("clear")
    sorted_words = sorted(wordFreqDict.iteritems(), key=lambda x: int(x[1]))
    for i in range(topWords):
        print(sorted_words.keys[i] + ":\t" + ("\u2588" * sorted_words.values[i]))

printStats(sampleText, 3)
