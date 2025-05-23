
from tagEachGender import isFemale_or_Male, isFemale_or_Neuter, isMale, isFemale, isNeuter

def tagGender(sentence):

    predictedTags = []

    wordList = sentence.split(" ")
    for word in wordList:
        tag = findGenTag(word)
        predictedTags.append(tag)

    return predictedTags


def findGenTag(word):

    flag1 = False
    flag2 = False

    if(isFemale_or_Male(word)):
        flag1 = True
    
    if(isFemale_or_Neuter(word)):
        flag2 = True
        
    if(flag1 or flag2):
        if(flag1 and flag2):
            return "any"
        elif(flag1):
            return "fm"
        else:
            return "fn"
    
    if(isFemale(word)):
        return "f"
    
    if(isMale(word)):
        return "m"
    
    if(isNeuter(word)):
        return "n"
    
    return "na"

