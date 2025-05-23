def isNominative(word, wordIndex, tagList):
    suffixList = ["డు", "ము", "వు", "లు"]
    if(len(word)>=2 and (word[-2:] in suffixList)):
        if (tagList[wordIndex]=="NA"):
            tagList[wordIndex]="Pr.vi-Nom"

def isAccusative(word, wordIndex, tagList):
    suffixList = ["ని", "ను", "ల", "కూర్చి", "గూర్చి", "గురించి"]
    if (len(word)>=2 and (word[-2:] in suffixList)):
        if (tagList[wordIndex]=="NA"):
            tagList[wordIndex]="Dvi.vi-Acc"
    elif(len(word)>=1 and (word[-1:] in suffixList)):
        if (tagList[wordIndex]=="NA"):
            tagList[wordIndex]="Dvi.vi-Acc"
    elif(len(word)>=6 and (word[-6:] in suffixList)):
        if (tagList[wordIndex]=="NA"):
            tagList[wordIndex]="Dvi.vi-Acc"
    elif(len(word)>=7 and (word[-7:] in suffixList)):
            tagList[wordIndex]="Dvi.vi-Acc"
    

def isInstrumental(word, wordIndex, tagList):
    suffixList = ["చేత", "చే", "తోడ", "తో"]
    if (len(word)>=2 and (word[-2:] in suffixList)):
        if (tagList[wordIndex]=="NA"):
            tagList[wordIndex]="Tru.vi-Inst"
    elif(len(word)>=3 and (word[-3:] in suffixList)):
            tagList[wordIndex]="Tru.vi-Inst"

def isDative(word, wordIndex, tagList):
    suffixList = ["కొరకు", "కై", "కోసం"]
    if (len(word)>=5 and (word[-5:] in suffixList)):
            tagList[wordIndex]="Cha.vi-Dat"
    elif (len(word)>=4 and (word[-4:] in suffixList)):
            tagList[wordIndex]="Cha.vi-Dat"
    elif (len(word)>=2 and (word[-2:] in suffixList)):
            tagList[wordIndex]="Cha.vi-Dat"

def isAblative(word, wordIndex, tagList):
    suffixList = ["వలన", "కంటే", "కంటె", "పట్టి"]
    if (len(word)>=3 and (word[-3:] in suffixList)):
            tagList[wordIndex]="Pan.vi-Abl"
    elif (len(word)>=4 and (word[-4:] in suffixList)):
            tagList[wordIndex]="Pan.vi-Abl"
    elif (len(word)>=5 and (word[-5:] in suffixList)):
            tagList[wordIndex]="Pan.vi-Abl"

def isGenitive(word, wordIndex, tagList):
    suffixList = ["కి", "కు", "యొక్క", "లో", "లోపల"]
    if (len(word)>=2 and (word[-2:] in suffixList)):
            tagList[wordIndex]="Sha.vi-Gen"
    elif (len(word)>=4 and (word[-4:] in suffixList)):
            tagList[wordIndex]="Sha.vi-Gen"
    elif (len(word)>=5 and (word[-5:] in suffixList)):
            tagList[wordIndex]="Sha.vi-Gen"

def isLocative(word, wordIndex, tagList):
    suffixList = ["అందు", "మందు", "యందు", "న"]
    if (len(word)>=1 and (word[-1:] in suffixList)):
        if (tagList[wordIndex]=="NA"):
            tagList[wordIndex]="Sap.vi-Loc"
    if (len(word)>=4 and (word[-4:] in suffixList)):
            tagList[wordIndex]="Sap.vi-Loc"

def isVocative(word, wordIndex, tagList):
    suffixList = ["ఓ", "ఓరి", "ఓరీ", "ఓయి", "ఓయీ", "ఓసి", "ఓసీ"]
    if (len(word)>=1 and (word[-1:] in suffixList)):
        if (tagList[wordIndex]=="NA"):
            tagList[wordIndex]="Sam.vi-Voc"
    if (len(word)>=3 and (word[-3:] in suffixList)):
            tagList[wordIndex]="Sam.vi-Voc"
