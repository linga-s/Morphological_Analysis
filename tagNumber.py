from tagEachNumber import isSingular, isPlural, isAny

def tagNumber(sentence):

    predictedTags = []

    wordList = sentence.split(" ")
    for word in wordList:
        tag = findNumTag(word)
        predictedTags.append(tag)

    return predictedTags


def findNumTag(word):

    if(isSingular(word)):
        return "sg"
    
    if(isPlural(word)):
        return "pl"
    
    if(isAny(word)):
       return "any"
    
    return "na"

