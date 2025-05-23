from findPOSTag import get_possible_tags_for_the_word

def tagSentence(sentence):

    tagsList = []
    sentenceList = sentence.split(" ")

    for word in sentenceList:
        templist = get_possible_tags_for_the_word(word)
        if(len(templist)==0):
            tagsList.append(["NA"])
        else:
            tagsList.append(templist)
    
    return tagsList

inputString = ""
print(tagSentence(inputString))