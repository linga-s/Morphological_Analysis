def isPlural(word):

    prefixList = ["ఎవర" ,"వారు", "వారి", "వారె", "వీరి", "వాళ్ళ", "వాళ్ల", "అందర", "మీరు", "మీతో", "మనం"]
    
    suffixList = ["క్కారు", "కోరు", "గారు", "చరు", "చారు", "ాయి", "ారు", "చ్చారు", "తారు", "శాము", "సాము", "తారో", "త్తారు", "ారట",
            "టారు", "ట్టారు", "డరు", "డ్డారు", "నారు", "న్నారు", "ప్పారు", "మంది",
           "యారు", "య్యారు", "రారు", "లారు", "లేరు", "శారు", "సారు", "స్తారు",]
    
    for pattern in prefixList:
        if word.startswith(pattern):
            return True


    for pattern in suffixList:
        if word.endswith(pattern):
            return True
        
    return False


def isSingular(word):

    prefixList = ["అతన", "అతడ", "అదే", "అది", "ఆమె", "ఆవిడ", 
                  "ఇతన", "ఇది", "ఇదే", "ఈమె", "ఈవిడ",
                    "ఎవడ", "ఉన్నాడ", "కుమారు", "నేను",
                  "దీని", "దేవుడ", "ప్రభూ", "ప్రభువ", "భగవ", "భూమి", 
                  "రాజు", "వాడు", "వాడి", "వీడి", "సోదర",]

    suffixList = ["ఉంది", "ంది", "కాడు", "గడు", "గాడు", "చింది", "చాడు",
                   "తాడు", "తుడు", "టడు", "టాడు", "ట్టాడు", "టాడట", "డాడు",
                     "నడు", "నాడు", "న్నాడు",
                     "పడడు", "పాడు", "ప్పాడు", "మ్మాడు", 
                   "యడు", "య్యడు", "యాడు", "య్యాడు", "రుడు", "రాడు", 
                   "వాడు", "వాడి", "శాడు", "సాడు", "స్తాడు", "స్తాను"]

    completeWords = ["ఉంది"]

    for pattern in prefixList:
        if word.startswith(pattern):
            return True

    for pattern in suffixList:
        if word.endswith(pattern):
            return True
    
    if word in completeWords:
        return True
    
    return False





def isAny(word):

    possible_tags_list = set()

    V_VM_VF_list = ["ాడు", "ారు", "ాయి", "ంది", "ాలి"]
    for pattern in V_VM_VF_list:
        if word.endswith(pattern):
            possible_tags_list.add("V_VM_VF")
            return True
    
    V_VM_VNF_list = ["తున్న", "ప్పుడు", "ించి", "కుండా", "ించే", "ంటే", "ిన", 
                     "తూ", "తే", "కొని", "ందుకు", "నట్లు", "కునే", "ినా", "ుకుని", "ేలా", "ల్సి", "ున్న", "పోయి"]

    for pattern in V_VM_VNF_list:
        if word.endswith(pattern):
            possible_tags_list.add("V_VM_VNF")
            return True

        
    V_VM_VNG_list = ["డం", "డం", "టం", "వటం", "గడం", "యడం", "ంతో", "టకు", "టమే", "డమే", "ానికి", "టంలో", "డంలో"]

    for pattern in V_VM_VNG_list:
        if word.endswith(pattern):
            possible_tags_list.add("V_VM_VNG")
            return True

    
    return False