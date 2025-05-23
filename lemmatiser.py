import os
import unicodedata

from tagEachNumber import isSingular


import re

sunna = "ం"
lu = "లు"
chi = "చి"
gaa = "గా"
lo = "లో"
lni = "ల్ని"
che = "చే"
nu = "ను"
du = "డు"
ni = "ని"
tho = "తో"
mdhi = "ంది"
sthu = "స్తూ"
na = "న"
aithvam = "ై"
ki = "కి"


def Lemmatizer(word):
    newSuffix = ""
    rootForm = word
    previouslyMatched = "No"

    if (len(word) >= 1 and word[-1] == sunna):
        if (len(word) >= 5):
            if (word[-5:] == "కోవటం"):
                newSuffix = "కొను"
                rootForm = word[:-5] + newSuffix
                previouslyMatched = "Yes"

            elif (word[-5:] == "పోవడం"):
                newSuffix = "పోవు"
                rootForm = word[:-5] + newSuffix
                previouslyMatched = "Yes"

        if (len(word) >= 3):
            if (word[-3:] == "చడం"):
                newSuffix = "చు"
                rootForm = word[:-3] + newSuffix
                previouslyMatched = "Yes"

        if (len(word) >= 5 and previouslyMatched == "No"):
            if (word[-5:] == "చ్చాం"):
                newSuffix = "చ్చు"
                rootForm = word[:-5] + newSuffix

    #            ================================= END OF THE RULE 1 =============================

    elif (len(word) >= 2 and word[-2:] == lu):
        if (len(word) >= 3):
            if (len(word) >= 5 and word[-5:] == "్నులు"):
                rootForm = word[:-2]
            elif (word[-3:] == "ులు"):
                newSuffix = "ి"
                rootForm = word[:-3] + newSuffix
            elif (word[-3:] == "ాలు"):
                newSuffix = "ం"
                rootForm = word[:-3] + newSuffix
            elif (len(word) > 4 and word[-4:] == "ట్లు"):
                newSuffix = "ట్లు"
                rootForm = word[:-4] + newSuffix
            elif (len(word) > 4 and word[-4:] == "ళ్లు"):
                newSuffix = "లు"
                rootForm = word[:-4] + newSuffix
            elif (word[-3:] == "్లు"):
                newSuffix = "ు"
                rootForm = word[:-3] + newSuffix
            else:
                rootForm = word[:-2]

    
    #            ================================= END OF THE RULE 2 =============================

    elif (len(word) >= 2 and word[-2:] == chi):
        if (len(word) >= 3 and word[-3:] == "చి"):
            newSuffix = "ుచు"
            rootForm = word[:-3] + newSuffix
        else:
            newSuffix = "చు"
            rootForm = word[:-2] + newSuffix

    #            ================================= END OF THE RULE 3 =============================
    
    elif (len(word) >= 2 and word[-2:] == gaa):
        if (len(word) >= 4):
            if (word[-4:] == "లుగా"):
                newSuffix = "లు"
                rootForm = word[:-2]
                rootForm = Lemmatizer(rootForm)
            elif (word[-4:] == "లాగా"):
                rootForm = word[:-4]
            elif (word[-4:] == "గ్గా"):
                newSuffix = "కు"
                rootForm = word[:-4] + newSuffix
            elif (word[-4:] == "లోగా"):
                newSuffix = "లో"
                rootForm = word[:-4] + newSuffix
                rootForm = Lemmatizer(rootForm)
            else:
                rootForm = word[:-2]

    #            ================================= END OF THE RULE 4 =============================

    elif (len(word) >= 2 and word[-2:] == lo):
        if (len(word) >= 7):
            if (word[-7:] == "ళ్లల్లో"):
                newSuffix = "ళ్లు"
                previouslyMatched = "Yes"
            rootForm = word[:-7] + newSuffix
            rootForm = Lemmatizer(rootForm)
        if (len(word) >= 6 and word[-6:] == "్లల్లో"):
            rootForm = word[:-4]
            newSuffix = "ు"
            rootForm = rootForm + newSuffix
            rootForm = Lemmatizer(rootForm)
            previouslyMatched = "Yes"
        if (previouslyMatched == "No" and len(word) >= 4 and word[-4:] == "ల్లో"):
            newSuffix = "లు"
            rootForm = word[:-4] + newSuffix
            previouslyMatched = "Yes"
        if (previouslyMatched == "No" and len(word) >= 3 and word[-3:] == "లలో"):
            newSuffix = "లు"
            rootForm = word[:-3] + newSuffix
            rootForm = Lemmatizer(rootForm)
            previouslyMatched = "Yes"
        if(len(word)>=3 and word[-3:] == "ంలో"):
            rootForm = word[:-3]
            previouslyMatched = "Yes"
        if (previouslyMatched == "No"):
            rootForm = word[:-2]

    elif (len(word) >= 4 and word[-4:] == "ళ్లు" ):
        if (len(word) >= 6):
            if (word[-6:] == "వాళ్ళు"):
                newSuffix = "వాడు"
                rootForm = word[:-6] + newSuffix

    #            ================================= END OF THE RULE 5 =============================

    elif (len(word) >= 4 and word[-4:] == lni):
        if (len(word) >= 5):
            if (word[-5:] == "ాల్ని"):
                newSuffix = "ం"
                previouslyMatched = "Yes"
            elif (word[-5:] == "ుల్ని"):
                newSuffix = "ి"
                previouslyMatched = "Yes"
            rootForm = word[:-5] + newSuffix
        if (previouslyMatched == "No"):
            rootForm = word[:-4]

    #            ================================= END OF THE RULE 6 =============================

    elif (len(word) >= 2 and word[-2:] == che):
        if (len(word) >= 3):
            if (word[-3:] == "ిచే"):
                newSuffix = "ుచు"
                rootForm = word[:-3] + newSuffix
            else:
                newSuffix = "ు"
                rootForm = word[:-1] + newSuffix

    #            ================================= END OF THE RULE 7 =============================

    elif (len(word) >= 2 and word[-2:] == nu):
        if (len(word) >= 6 and word[-6:] == "స్తాను"):
            newSuffix = "ంచు"
            rootForm = word[:-6] + newSuffix
        elif (len(word) >= 5 and word[-5:] == "డతాను"):
            newSuffix = "ట్టు"
            rootForm = word[:-5] + newSuffix
        elif (len(word) >= 4 and word[-4:] == "తాను"):
            newSuffix = ""
            rootForm = word[:-4] + newSuffix
        elif (len(word) >= 4 and word[-4:] == "యాను"):
            newSuffix = "వు"
            rootForm = word[:-4] + newSuffix
        elif (len(word) >= 6 and word[-6:] == "న్నాను"):
            newSuffix = "న్ను"
            rootForm = word[:-6] + newSuffix
        elif (len(word) >= 6 and re.search(".*ి.ాను$", word)):
            newSuffix = word[-6] + "ు" + word[-4] + "ు"
            rootForm = word[:-6] + newSuffix
        elif (len(word) >= 3 and word[-3:] == "ాను"):
            newSuffix = "ు"
            rootForm = word[:-3] + newSuffix
        elif (len(word) >= 3 and word[-3:] == "లను"):
            newSuffix = "లు"
            rootForm = word[:-3] + newSuffix
            rootForm = Lemmatizer(rootForm)
        elif (len(word) >= 5 and word[-5:] == "నన్ను"):
            rootForm = word
        else:
            rootForm = word[:-2]
            rootForm = Lemmatizer(rootForm)

    #            ================================= END OF THE RULE 8 =============================

    elif (len(word) >= 2 and word[-2:] == du):
        if (len(word) >= 6 and re.search(".*ి.ాడు$", word)):
            newSuffix = word[-6] + "ు" + word[-4] + "ు"
            rootForm = word[:-6] + newSuffix
        elif (len(word) >= 5 and word[-5:] == "్నాడు"):
            newSuffix = "ను"
            rootForm = word[:-5] + newSuffix
        elif (len(word) >= 4 and word[-4:] == "తాడు"):
            rootForm = word[:-5]
        elif (len(word) >= 4 and word[-4:] == "యాడు"):
            newSuffix = "వు"
            rootForm = word[:-4] + newSuffix
        elif (len(word) >= 4 and word[-4:] == "శాడు"):
            newSuffix = "యు"
            rootForm = word[:-4] + newSuffix
        elif (len(word) >= 6 and word[-6:] == "డ్డాడు"):
            newSuffix = "డు"
            rootForm = word[:-6] + newSuffix
        elif (len(word) >= 3 and word[-3:] == "ాడు"):
            newSuffix = "ు"
            rootForm = word[:-3] + newSuffix
        elif (len(word) >= 6 and re.search(".*ి.ేడు$", word)):
            newSuffix = word[-6] + "ు" + word[-4] + "ు"
            rootForm = word[:-6] + newSuffix
        elif (len(word) >= 3 and word[-3:] == "ేడు"):
            newSuffix = "ు"
            rootForm = word[:-3] + newSuffix

    #            ================================= END OF THE RULE 9 =============================

    elif (len(word) >= 2 and word[-2:] == ni):
        if (len(word) >= 4 and word[-4:] == "కుని"):
            newSuffix = "కొను"
            rootForm = word[:-4] + newSuffix
        elif (len(word) >= 5 and word[-5:] == "ాన్ని"):
            newSuffix = "ం"
            rootForm = word[:-5] + newSuffix
        elif (len(word) >= 4 and word[-4:] == "న్ని"):
            rootForm = word
        elif (len(word) >= 3 and word[-3:] == "్ని"):
            newSuffix = "ు"
            rootForm = word[:-3] + newSuffix
        elif (len(word) >= 6 and word[-6:] == "క్కొని"):
            newSuffix = "గు"
            rootForm = word[:-6] + newSuffix
        elif (len(word) >= 6 and word[-6:] == "క్కొని"):
            newSuffix = "గు"
            rootForm = word[:-6] + newSuffix
        elif (len(word) >= 4 and word[-4:] == "కుని"):
            newSuffix = ""
            rootForm = word[:-4] + newSuffix
        elif (len(word) >= 4 and word[-4:] == "లోని"):
            newSuffix = "లో"
            rootForm = word[:-4] + newSuffix
            rootForm = Lemmatizer(rootForm)
        elif (len(word) >= 3 and word[-3:] == "లని"):
            newSuffix = "ు"
            rootForm = word[:-2] + newSuffix
            rootForm = Lemmatizer(rootForm)
        elif (len(word) >= 2 and word[-2:] == "ని"):
            newSuffix = ""
            rootForm = word[:-2] + newSuffix


    #            ================================= END OF THE RULE 10 =============================

    elif(len(word)>=2 and word[-2:] == tho):
        if (len(word) >= 4 and word[-4:] == "ాలతో"):
            newSuffix = "ాలు"
            rootForm = word[:-4] + newSuffix
            rootForm = rootForm[:-3]
            rootForm += 'ం'
        elif (len(word) >= 3 and word[-3:] == "లతో"):
            newSuffix = "లు"
            rootForm = word[:-3] + newSuffix
            rootForm = Lemmatizer(rootForm)
        elif (len(word) >= 4 and word[-4:] == "ల్తో"):
            newSuffix = "లు"
            rootForm = word[:-3] + newSuffix
            rootForm = Lemmatizer(rootForm)
        elif (len(word) >= 4 and word[-4:] == "త్తో"):
            newSuffix = "తి"
            rootForm = word[:-4] + newSuffix
        else:
            rootForm = word[:-2]

    #            ================================= END OF THE RULE 11 =============================

    if (len(word) >= 1 and word[-1:] == "ల"):
        newSuffix = "ు"
        rootForm = word + newSuffix
        rootForm = Lemmatizer(rootForm)

    #            ================================= END OF THE RULE 12 =============================

    elif (len(word) >= 2 and word[-2:] == "కు"):
        if (len(word) >= 3 and word[-3:] == "లకు"):
            newSuffix = ""
            rootForm = word[:-3] + newSuffix
        else:
            rootForm = word[:-2]

    #            ================================= END OF THE RULE 13 =============================

    elif (len(word) >= 3 and word[-3:] == mdhi):
        if (len(word) >= 8 and re.search('.+ి.ింది$', word)):
            newSuffix = word[-7] + "ు" + word[-5] + "ు"
            rootForm = word[:-7] + newSuffix
        elif (len(word) >= 6 and word[-6:] == "ేసింది"):
            newSuffix = "ు"
            rootForm = word[:-7] + newSuffix
        elif (len(word) >= 5 and word[-5:] == "యింది"):
            newSuffix = "వు"
            rootForm = word[:-6] + newSuffix
        elif (len(word) >= 4 and word[-4:] == "ింది"):
            newSuffix = "ు"
            rootForm = word[:-5] + newSuffix
        elif (len(word) >= 5 and word[-5:] == "తుంది"):
            newSuffix = "వు"
            rootForm = word[:-5] + newSuffix
        elif (len(word) >= 4 and word[-4:] == "ొంది"):
            newSuffix = "ను"
            rootForm = word[:-3] + newSuffix


    #            ================================= END OF THE RULE 14 =============================

    elif (len(word) >= 4 and word[-4:] == sthu):
        if (len(word) >= 5 and word[-5:] == "ుస్తూ"):
            newSuffix = "ుపు"
            rootForm = word[:-5] + newSuffix
        elif (len(word) >= 5 and word[-5:] == "ూస్తూ"):
            newSuffix = "ూడు"
            rootForm = word[:-5] + newSuffix
        elif (len(word) >= 5 and word[-5:] == "ిస్తూ"):
            newSuffix = "ించు"
            rootForm = word[:-4] + newSuffix
        else:
            newSuffix = "యు"
            rootForm = word[:-4] + newSuffix


    #            ================================= END OF THE RULE 15 =============================

    elif (len(word) >= 1 and word[-1:] == na):
        if (len(word) >= 6 and re.search('.+ి.ిన$', word)):
            newSuffix = "ు" + word[-3] + "ు"
            rootForm = word[:-4] + newSuffix
        elif (len(word) >= 6 and word[-6:] == "ాల్సిన"):
            newSuffix = "ు"
            rootForm = word[:-6] + newSuffix
        elif (len(word) >= 3 and word[-3:] == "సిన"):
            newSuffix = "యు"
            rootForm = word[:-3] + newSuffix
        elif (len(word) >= 3 and word[-3:] == "యిన"):
            newSuffix = "వు"
            rootForm = word[:-3] + newSuffix
        elif (len(word) >= 2 and word[-2:] == "ిన"):
            newSuffix = "ు"
            rootForm = word[:-2] + newSuffix
        elif (len(word) >= 2 and word[-2:] == "ైన"):
            newSuffix = "ు"
            rootForm = word[:-2] + newSuffix
        elif (len(word) >= 2 and word[-2:] == "ున"):
            rootForm = word[:-1]

            #            ================================= END OF THE RULE 16 =============================

    elif (len(word) >= 1 and word[-1:] == aithvam):
        if (len(word) >= 3 and word[-3:] == "లపై"):
            newSuffix = "ు"
            rootForm = word[:-2] + newSuffix
            rootForm = Lemmatizer(rootForm)
        elif (len(word) >= 2 and word[-2:] == "పై"):
            rootForm = word[:-2]
        elif (len(word) >= 1 and word[-1:] == "ై"):
            newSuffix = "ు"
            rootForm = word[:-1] + newSuffix

            #            ================================= END OF THE RULE 17 =============================


    elif (len(word) >= 2 and word[-2:] == ki):
        if (len(word) >= 3 and word[-3:] == "లకి"):
            rootForm = word[:-2]
            rootForm = rootForm + 'ు'
            rootForm = Lemmatizer(rootForm)
        elif (len(word) >= 5 and word[-5:] == "ానికి"):
            newSuffix = "ం"
            rootForm = word[:-5] + newSuffix
            rootForm = Lemmatizer(rootForm)
        elif (len(word) >= 3 and word[-3:] == "ికి"):
            newSuffix = "ు"
            rootForm = word[:-3] + newSuffix
        elif (len(word) >= 4 and word[-4:] == "లోకి"):
            rootForm = word[:-4]
        else:
            rootForm = word[:-2]

            #            ================================= END OF THE RULE 18 =============================

    return (rootForm)

