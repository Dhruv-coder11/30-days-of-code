def greatestCommonFactor(whiteC, redC):
    return whiteC if(redC == 0) else greatestCommonFactor(redC, whiteC % redC)

redCorpuscles = 5000000
whiteCorpuscles = 8000

factor = greatestCommonFactor (whiteCorpuscles, redCorpuscles)

whiteRatio = int(whiteCorpuscles/factor)
redRatio = int(redCorpuscles/factor)

print("Aspect Ratio:", whiteRatio,":",redRatio)