def splitText(text):
    finalList = []
    word = ""
    for charIndex in range(len(text)):
        # Triggers if the character is a number or a letter
        if text[charIndex].isalnum():
            word = word + text[charIndex]
            if charIndex == len(text) - 1:
                finalList.append(word)
                break
        elif not word == "":
            finalList.append(word)
            word = ""
        else:
            word = word + text[charIndex]
    return finalList


def getWordStartingWith(inputText, letter):
    wordList = splitText(inputText)
    finalDict = {}
    for word in wordList:
        if word[0].lower() == letter.lower():
            finalDict[word] = True
    return list(finalDict.keys())


def printWordsFrequency(inputText, letter):
    wordList = splitText(inputText)
    finalDict = {}
    for word in wordList:
        if word[0].lower() == letter.lower():
            if word in finalDict:
                finalDict[word] += 1
            else:
                finalDict[word] = 1
    for entry in finalDict:
        print('"'+ entry + '" occurs ' + str(finalDict[entry]) + ' times.')


def getWordFrequency(inputText, letter):
    wordList = splitText(inputText)
    finalDict = {}
    for word in wordList:
        if word[0].lower() == letter.lower():
            if word in finalDict:
                finalDict[word] += 1
            else:
                finalDict[word] = 1
    return finalDict
