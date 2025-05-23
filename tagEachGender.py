def isFemale_or_Male(word):

    prefixList = ["అందర", "ఎవర" ,"వారు", "వారి", "వారె", "వీరి", "వాళ్ళ", "వాళ్ల", "మేమ", "మనం", "మీరు", "నేన", ]
    
    suffixList = ["కరు", "క్కారు", "కోరు", "గారు", "చరు", "చారు", "చ్చారు", "తారు", "తారో", "త్తారు", "ారట", 
            "టారు", "ట్టారు", "డరు", "డను", "డ్డారు", "నారు", "న్నారు", "ప్పారు",
           "యారు", "య్యారు", "రారు", "పారు", "లారు", "లేరు", "శారు", "సారు", "స్తారు", "స్తాను", "న్నాను"]
    

    completeWords = ["మా", "మేము", "మీకు", "మీరు", "నన్ను", "నేను"]

    for pattern in prefixList:
        if word.startswith(pattern):
            return True

    for pattern in suffixList:
        if word.endswith(pattern):
            return True
    
    if word in completeWords:
        return True
    
    return False


def isFemale_or_Neuter(word):

    suffixList = ["ింది", "ినది", "ుంది", "ొంది", "ోంది", "ందని", "ందో", "ండదు", "కదు", "గదు", "ంచదు",
                   "తాయి", "ట్టదు", "పోదు", "డదు", "రాదు", "లదు", "వదు", "న్నది", "నదని", "ున్నది", "స్తుందా"]

    prefixList = ["అదె", "ఇదె", "ఉంద", "ఏవి", "ఏదో", "దని", "దీని", "దీనిక", "దాంతో", "దాని", "దాన్ని", "దేని", "వాటి", "వీటి",]

    completeWords = ["అది", "అదే", "అవి", "అవే", "ఇది", "ఉంది", "కలదు", "లేదు", "ఉండదు"]

    for pattern in prefixList:
        if word.startswith(pattern):
            return True

    for pattern in suffixList:
        if word.endswith(pattern):
            return True
    
    if word in completeWords:
        return True
    
    return False


def isFemale(word):

    prefixList = ["అదే", "అది", "ఆమె", "ఆవిడ", "ఇది", "ఇదే", "ఈమె", "ఈవిడ", "దీని", "భూమి", "దేవత"]

    suffixList = ["చింది", "ఉంది"]

    completeWords = ["ఉంది", "ఉండదు", "గంగా", "గంగానది", "తల్లి", "పార్వతీదేవి", "యమునా", "విద్య",]

    for pattern in prefixList:
        if word.startswith(pattern):
            return True

    for pattern in suffixList:
        if word.endswith(pattern):
            return True
    
    if word in completeWords:
        return True
    
    return False


def isMale(word):

    prefixList = ["అతన", "ఇతన", "ఎవడ", "ఉన్నాడ", "కుమారు", 
                  "దేవుడ", "ప్రభూ", "ప్రభువ", "భగవ", 
                  "రాజు", "వాడు", "వాడి", "వీడి", "సోదర"]

    suffixList = ["కాడు", "గడు", "గాడు", "చాడు",
                   "తాడు", "తుడు", "టడు", "టాడు", "ట్టాడు", "టాడట", "డాడు",
                     "నడు", "నాడు", "న్నాడు",
                     "పడడు", "పాడు", "ప్పాడు", "మ్మాడు", 
                   "యడు", "య్యడు", "యాడు", "య్యాడు", "రుడు", "రాడు", 
                   "వాడు", "వాడి", "శాడు", "శుడు", "సాడు", "స్తాడు"]


    completeWords = ["ఆదినాథ్", "ఆర్యులుగా", "చంద్ర", "చక్రవర్తులు", "చరిత్రకారులు", "చేసుకుంటాడట", "చౌహానులూ", 
                 "బాహుబలి", "మహారాజు", "తమ్ముడు", "పాండవులకు", "బతిమాలాడు", "బాదాడు", "ప్రజలు", "పారిపోయాడని", "ముఖ్యమంత్రిగా", 
                 "రామ", "రాజపుత్రులూ", "వినడు", 
                  "శంకర", "శిబి", "శివ", "శ్రీచంద్ర", "శంకరుణ్ణి", "సోమయశుడు"]
    

    for pattern in prefixList:
        if word.startswith(pattern):
            return True


    for pattern in suffixList:
        if word.endswith(pattern):
            return True
        
    if word in completeWords:
        return True
    
    return False
    

def isNeuter(word):

    suffixList = ["కావు", "గాయి", "చవు", "చాయి", 
                  "తాయి", "తాయా", "టాయి", "డాయి", "డవు", "నవు", "నాయి", "న్నాయి", 
                  "యాయి", "యెను", "లలో", "లతో", "లుగా", "లాయి", "లేవు", "ంలో",
                    "రవు", "రావు", "రావా", "రాయి", "శాయి", "ఉంది"]
    
    completeWords = ["రావని"]

    for pattern in suffixList:
        if word.endswith(pattern):
            return True
        
    if word in completeWords:
        return True
    
    return False

    


