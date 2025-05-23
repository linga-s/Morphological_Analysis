def tagPerson(sentence):

    predictedTags = []

    wordList = sentence.split(" ")
    for word in wordList:
        tag = getPerson(word)
        predictedTags.append(tag)

    return predictedTags


def getPerson(word):
    
    if word in ["నేను", "మేము", "మనం", "మా", "నన్ను", "నాకు"]:
        return "Fp"
    
    if word.startswith in ["నేన", "మేమ", ]:
        return "Fp"
    
    if word in ["నీవు", "మీరు", "నువ్వు", "మీతో", "మీకు", "మీ", "మీకు", "నీకు"]:
        return "Sp"
    
   
    if word in ["అతడు", "అతను", "ఆయన", "ఆమె", "ఈమె", "ఆవిడ", "ఇది", "అది", "వారు", "వాళ్ళు", "ఇవి", "అవి", "అదే",
                "ఇదే", "ఈవిడ", "వాడు", ]:
        return "Tp"
    
    if word.startswith(("అతన", "అతడ",
                       "ఇతన", "వారి", "వారె", "వీరి", "వాళ్ళ", "వాళ్ల", "దీని", "దీనిక", "దాంతో", "దాని", "దాన్ని",
                     "వాడి", "వీడి", "అదె", "ఇదె", "వాటి", "వీటి", "అవే", )):
        return "Tp"

    return "NA"



