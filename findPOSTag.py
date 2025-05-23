from POS_Model import tag_POS 

verb_tags = ['V_VM_VF', 'V_VAUX']
verbal_tags = ['V_VM_VNF', 'V_VM_VINF', 'V_VM_VNG', 'N_NNV']
naming_word_tags = [
    'N_NN', 'N_NNP', 'N_NST',
    'PR_PRP', 'PR_PRF', 'PR_PRL', 'PR_PRC', 'PR_PRQ',
    'DM_DMD', 'DM_DMR', 'DM_DMQ',
    'JJ', 'RB', 'PSP',
    'CC_CCD', 'CC_CCS', 'CC_CCS_UT',
    'RP_RPD', 'RP_CL', 'RP_INJ', 'RP_INTF', 'RP_NEG',
    'QT_QTF', 'QT_QTC', 'QT_QTO',
    'RD_RDF', 'RD_SYM', 'RD_PUNC', 'RD_UNK', 'RD_ECH'
]

def get_possible_tag_for_the_word(word):
    
    possible_tags_list = set()

    current_tags = isPronoun(word)
    for tag in current_tags:
        possible_tags_list.add(tag)
    
    if(len(current_tags)!=0):
        return possible_tags_list
    
    current_tags = isDemonstrative(word)
    for tag in current_tags:
        possible_tags_list.add(tag)
    
    if(len(current_tags)!=0):
        return possible_tags_list
    
    current_tags = isVerb(word)
    for tag in current_tags:
        possible_tags_list.add(tag)
    
    if(len(current_tags)!=0):
        return possible_tags_list
    
    current_tags = isAdjective(word)
    for tag in current_tags:
        possible_tags_list.add(tag)
    
    if(len(current_tags)!=0):
        return possible_tags_list
    
    current_tags = isAdverb(word)
    for tag in current_tags:
        possible_tags_list.add(tag)
    
    if(len(current_tags)!=0):
        return possible_tags_list
    
    current_tags = isPostposition(word)
    for tag in current_tags:
        possible_tags_list.add(tag)
    
    if(len(current_tags)!=0):
        return possible_tags_list
    
    current_tags = isConjunction(word)
    for tag in current_tags:
        possible_tags_list.add(tag)
    
    if(len(current_tags)!=0):
        return possible_tags_list
    
    current_tags = isParticle(word)
    for tag in current_tags:
        possible_tags_list.add(tag)
    
    if(len(current_tags)!=0):
        return possible_tags_list

    current_tags = isQuantifier(word)
    for tag in current_tags:
        possible_tags_list.add(tag)
    
    if(len(current_tags)!=0):
        return possible_tags_list
    
    current_tags = isResidual(word)
    for tag in current_tags:
        possible_tags_list.add(tag)

    if(len(current_tags)!=0):
        return possible_tags_list
    
    return possible_tags_list



#No patterns found for Nouns
    
def isPronoun(word):

    possible_tags_list = set()
    personal_pronouns_list = ["అవి", "అందులో", "అతన", "అతడ", "ఆయన", "ఆమె", "అద", "అవే", "అదే", "అందు", "అతణ్",
                              "ఇవ", "ఇద", "ఇదం", "ఇతడ", "ఇందు", "ఇతన", "ఇతర",
                              "ఈమె", "ఈయన", "ఈతన", "ఈతడ",
                              "ఏది", "ఎదుటివార", 
                              "తాన", "తన", "తమ", "తామ",
                              "నిన్ను", "నన్", "నిన్", "నేన", "నేనూ","నువ్వు", "నాకి", "నాకు", "నాకే", "నాతో", "నాపై", "నాది", "నాలో", "నువ్", "నాకం", "నీతో", 
                              "మన", "మీకు","మీరు", "మేము", "మీకం", "మేం", "మాకు", "మీరూ", "మీరు", "మాతో", "మేమ్", "మేమ", "మీర", "మమ్మల్",
                              "దీని", "దీన్","దాని", "దీంతో", "దాం", "దాన్", "దేన్",
                              "వీ. టి", "వీరు", "వీరూ", "వారు", "వారూ", "వారంతా","వారి", "వాళ్", "వాళ్ళ", "వీళ్",
                              "వాని", "వాడి", "వాడు", "వాటి", "వారే", "వీరో", "వీరంతా", "వాటి", "వాటీ", "వీరి", "వీరీ", "వారంద", "వారో", "వేటిక", 
                              ]
    personal_pronoun_complete_words = ["ఆ", "ఈ", "నా", "నీ", "మీ", "మా", "మీలాంటి", "తద్వారా", "అంతే", "వీటన్నిటి", "నాకెంతో", "అంతగా", "అంత"]
    
    for pattern in personal_pronouns_list:
        if word.startswith(pattern):
            possible_tags_list.add("PR_PRP")
            break

    if word in personal_pronoun_complete_words:
        possible_tags_list.add("PR_PRP")


    reflexive_pronoun = ["స్వయంగా" , "స్వయం" ,"స్వయానా", "స్వయాన", "తన"] #Ourselves
    for pattern in reflexive_pronoun:
        if word.startswith(pattern):
            possible_tags_list.add("PR_PRF")
            break


    relative_pronoun_list = ["ఎక్కడ", "ఏదైనా", "ఎప్పుడ", "ఎంద", "ఎంత", "ఎల", "ఏమిట", "ఏవ", "ఎన్", "ఏమై", "ఎమి",
                             "ఏనాడ", "ఏద", "ఎప్", "ఎవర", "ఎంద", "ఎటు", "ఏమ", "ఎద", "ఏమ", "ఏంటో", "ఎవ్", "ఏం",
                             "ఎవ", "ఎమిట", "ఏయే", "ఏల", "ఎట్", "ఏన్", "ఏపాటి", "ఎటూ", "ఆమె", "అతని", "దీనితో", "అదె"]
    
    relative_pronoun_complete_words = ["ఏ", "ఎ", "దాని", "వేటికి", "వేటికీ", "వీటికి"]

    for pattern in relative_pronoun_list:
        if word.startswith(pattern):
            possible_tags_list.add("PR_PRL")
            break
        
    if word in relative_pronoun_complete_words:
        possible_tags_list.add("PR_PRL")
    

    reciprocal_pronoun_list = ["పరస్పర", "పరస్పరం", "స్వయం"] #Eachother

    for pattern in reciprocal_pronoun_list:
        if word.startswith(pattern):
            possible_tags_list.add("PR_PRC")
            break

    
    wh_pronoun_list = ["ఎక్కడ", "ఏదైనా", "ఎప్పుడ", "ఎంద", "ఎంత", "ఎల", "ఏమిట", "ఏవ", "ఎన్", "ఏమై", "ఎమి",
                             "ఏనాడ", "ఏద", "ఎప్", "ఎవర", "ఎవర", "ఎంద", "ఎటు", "ఏమ", "ఎద", "ఏమ", "ఏంటో", "ఎవ్", "ఏం",
                             "ఎవ", "ఎమిట", "ఏయే", "ఏల", "ఎట్", "ఏన్", "ఏపాటి", "ఎటూ"]
    
    wh_pronoun_complete_words = ["ఏ", "ఎ", "దేన్ని"]  #Interrogative type

    wh_pronoun_ending_list = ["క్కడ"]

    for pattern in wh_pronoun_list:
        if word.startswith(pattern):
            possible_tags_list.add("PR_PRQ")
            break
    
    for pattern in wh_pronoun_ending_list:
        if word.endswith(pattern) and len(personal_pronoun_complete_words)!=0:
            possible_tags_list.add("PR_PRQ")
    
    if word in wh_pronoun_complete_words:
        possible_tags_list.add("PR_PRQ")
    
    
    return possible_tags_list

    #No words for Indefinite in PR_PRI

def isDemonstrative(word):

    possible_tags_list = set()
    deictic_list = ["ఆ", "ఈ", "ఈలోగా", "యా", "ఏ"]
    
    if word in deictic_list:
        possible_tags_list.add("DM_DMD")

    relative_list = ["ఏ", "ఏం", "ఏయే", "యే", "ఏఏ", "యేయే"]

    if word in relative_list:
        possible_tags_list.add("DM_DMR")
        
            
    
    #No enough words for DM_DMQ.
    #No words of DM_DMI at all.
    return possible_tags_list

def isVerb(word):

    possible_tags_list = set()

    V_VM_VF_list = ["ాడు", "ారు", "ాయి", "ంది", "ాలి", "న్నాను", "కరు", "క్కారు", "కోరు", "గారు", "చరు", "చాను", "చారు", "చ్చారు", "తారు", "తారో", "త్తారు", 
            "టారు", "ట్టారు", "డరు", "డను", "డ్డారు", "నారు", "న్నారు", "ప్పారు",
           "యారు", "య్యారు", "రారు", "లారు", "లేరు", "శారు", "లేదు", "ఉంది", "సారు", "స్తారు", "స్తాను", "న్నాను", "ాము", "సాను"]
    for pattern in V_VM_VF_list:
        if word.endswith(pattern):
            possible_tags_list.add("V_VM_VF")
            break
    
    V_VM_VNF_list = ["తున్న", "ప్పుడు", "ించి", "కుండా", "ించే", "ంటే", "ిన", 
                     "తూ", "తే", "కొని", "ందుకు", "నట్లు", "కునే", "ినా", "ుకుని", "ేలా", "ల్సి", "ున్న", "పోయి", "నికి"]

    for pattern in V_VM_VNF_list:
        if word.endswith(pattern):
            possible_tags_list.add("V_VM_VNF")
            break

        
    V_VM_VNG_list = ["డం", "డం", "టం", "వటం", "గడం", "యడం", "ంతో", "టకు", "టమే", "డమే", "ానికి", "టంలో", "డంలో", "కుంటూ"]

    for pattern in V_VM_VNG_list:
        if word.endswith(pattern):
            possible_tags_list.add("V_VM_VNG")
            break

    
    return possible_tags_list

def isAdjective(word):

    possible_tags_list = set()
    adjective_list = ["ైన", "ాన", "ైనా", "ౖన", "త్మక", "త్మిక" ,"మై", "యిన", "కర", "ిక", "పు", "ైతే", "ీయ", "ిత", "ాయ", "యా", "యని", "ంత", "తర", "టి", "య"]

    for pattern in adjective_list:
        if word.endswith(pattern):
            possible_tags_list.add("JJ")
            break

    return possible_tags_list

def isAdverb(word):

    possible_tags_list = set()

    adverb_list = ["ంగా", "ిగా", "ుగా", "ానే", "తగా"]
    for pattern in adverb_list:
        if word.endswith(pattern):
            possible_tags_list.add("RB")
            break
    
    return possible_tags_list

def isPostposition(word):

    possible_tags_list = set()

    postposition_patterns = ["వంటివ", "వద్ద", "లలో", "వల్ల", "ద్వారా", "మధ్య", "మేర", "మీద",
                              "వరక", "బయట", "గురించ", "పాటూ", "పాటు", "గూర్చి", "నుంచ", "కింద", "లతో", "దగ్గర", "వలన", "మాదిర"]

    
    postposition_list = ["ఆమేరకు",
                          "కోసం", "కంటే", "కొరకు", "కి", "కన్నా", "కన్న", "కే", "కాడికి", "కు", "కూ", "కల్లా", "కంటె", "క్రిందికే", "కోసమే", "కొరకే", "కొరకై",
                          "గా", "గుండా", "గుర్తించి", "గానూ", "గాను",
                          "చేత", "చే", "చొప్పున", "తోనే", "చుట్టు", "చుట్టూ",
                          "తో", "తోపాటు", "తరపున", "తద్వారా",  
                          "దాకా", "ద్వార",
                          "ను", "న", "నూ", "ని", "నుండి", "నుండీ", "నుండే",
                          "టు", 
                          "పాటు", "పాటే", "పాటు", "ప్రకారం", "పట్ల", "పైగా", "పై", 
                          "బట్టి", "బట్టే", "బారిన",
                          "మేర", "ముందుకు", "ముందే",
                          "యొక్క", 
                          "లు", "ల", "లోనూ", "ల్లోనూ", "ల్లో", "లోనే", "లోని", "లోకి", "లోపు", "లో", "లోన", "లను", "లకు",
                            "లాగా", "లోగా", "లోపే", "లోపల", "లపై", "లతో", "లాంటి", "లవల్ల", "లాంటివి", "లోనికి", "లోంచి", "లోపలే", "లోపు",
                          "వ", "వంటి", "వలన", "వద్ద", "వద్దకు", "వైపు", "వల్లనే", "వలె", "వలెనే", "వైపే", "వలనే", "వలే",
                           "సరికి", "సరసన", "ికి"]
    
    
    for pattern in postposition_patterns:
        if(word.startswith(pattern)):
            possible_tags_list.add("PSP")
            break
        
    for pattern in postposition_list:
        if word.endswith(pattern):
            possible_tags_list.add("PSP")
            break

    return possible_tags_list

def isConjunction(word):

    possible_tags_list = set()

    CC_CCD_list = ["లేదా", "కానీ", "కాని", "అందువల్ల", "గాని", "గానీ", "మరియు"]

    if word in CC_CCD_list:
        possible_tags_list.add("CC_CCD")

    CC_CCS_list = ["అనేది", "అనే", "అనగా", "ఒకవేళ", "అందుకని", "అందుకే", "అంటే", "అన్నదీ", "కాబట్టి", "అందుకనే", "అందుకోసం", "అందుకోసమే", "అనగా", "అనగానే", "అనేదే", "అందుకు"]

    if word in CC_CCS_list:
        possible_tags_list.add("CC_CCS")

    CC_CCS_UT_list = ["అని", "అనీ"]

    if word in CC_CCS_UT_list:
        possible_tags_list.add("CC_CCS_UT")

    return possible_tags_list

def isParticle(word):

    possible_tags_list = set()

    #No pattern found for RP_RPD
    
    RP_CL_list = ["మంది"]

    for pattern in RP_CL_list:
        if word.startswith(pattern):
            possible_tags_list.add("RP_CL")
            break
        
    RP_INJ_list = ["కదా", "గదా", "ఔరా", "బాబోయ్"]

    for pattern in RP_INJ_list:
        if word.startswith(pattern):
            possible_tags_list.add("RP_INJ")
            break
    
    #No pattern found for RP_INTF
        
    RP_NEG_list = ["తప్ప", "మినహా", "నాట్"]
    if word in RP_NEG_list:
        possible_tags_list.add("RP_NEG")
        
    return possible_tags_list

def isQuantifier(word):

    possible_tags_list = set()

    #No pattern found for QT_QTF

    num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for num in num_list:
        if ((num in word) and ("వ" not in word)):
            possible_tags_list.add("QT_QTC")
    

    QT_QTO_list = ["దవ", "డవ", "టవ", "రథమ", "రధమ", "డోవ", "తీయ", "వసారి"]

    for num in num_list:
        if ((num in word) and word.endswith("వ")):
            possible_tags_list.add("QT_QTO")
            break
    
    for pattern in QT_QTO_list:
        if word.endswith(pattern):
            possible_tags_list.add("QT_QTO")
            break
        
    return possible_tags_list

def isResidual(word):
    
    possible_tags_list = set()

    for char in word:
        if ord(char)>=65 and ord(char)<=91:
            possible_tags_list.add("RD_RDF")
            break
        if ord(char)>=97 and ord(char)<=123:
            possible_tags_list.add("RD_RDF")
            break
            

    RD_SYM_list = ["(", ")", "+", "/" ,"x"]

    if word in RD_SYM_list:     #There are some errors in the dataset. Same symbol (e.g., (.. ... is being classified as symbol as well as punctuation))
        possible_tags_list.add("RD_SYM")
        
    punctuation_list = [":", "\'", "\"", "?", ".", ",", "!", ";", "`", "-", "“", "”", "‘", "’", ""]
    for pattern in punctuation_list:
        if pattern == word:
            possible_tags_list.add("RD_PUNC")
            break

    #No words found for RD_UNK
    #No words found for RD_ECH
        
    return possible_tags_list
    


def TAGGING_POS(sentence):
    model_based_tags = tag_POS(sentence)
    sen_list = sentence.split()
    tags = list()
    index = 0
    for word in sen_list:
        tag = get_possible_tag_for_the_word(word)
        if(len(tag)!=0):
            if (all(elem in verb_tags for elem in tag)):
                tags.append("VB")
            elif (all(elem in verbal_tags for elem in tag)):
                tags.append("VBL")
            elif (all(elem in naming_word_tags for elem in tag)):
                tags.append("NW")
            else:
                tags.append(model_based_tags[index])
        else:
            tags.append(model_based_tags[index])
        index+=1
    return tags



