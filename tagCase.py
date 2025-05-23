from tagEachCase import isNominative, isAccusative, isInstrumental, isDative, isAblative, isGenitive, isLocative, isVocative
from tagPerson import getPerson
from findPOSTag import isVerb

def tagCase(sentence):
    wordList = sentence.split(" ")
    trim_chars = ".,!?;:\"'()[]{}<>"
    clean_words = [word.strip(trim_chars) for word in wordList]
    predictedTags = ["NA"] * len(clean_words)
    wordIndex = 0
    for word in clean_words:
        findTag(word, wordIndex, predictedTags)
        wordIndex+=1
    return predictedTags




def findTag(word, wordIndex, predictedTags):
    if(len(isVerb(word))>0):
        return
    isNominative(word, wordIndex, predictedTags)
    isAccusative(word, wordIndex, predictedTags)
    isInstrumental(word, wordIndex, predictedTags)
    isDative(word, wordIndex, predictedTags)
    isAblative(word, wordIndex, predictedTags)
    isGenitive(word, wordIndex, predictedTags)
    isLocative(word, wordIndex, predictedTags)
    isVocative(word, wordIndex, predictedTags)
    tag = getPerson(word)
    if(tag!="NA"):
        predictedTags[wordIndex] = "Pr.vi-Nom"
    