words = open('weakWords.txt', 'r')
wordsLst = words.read().split('\n')
print(wordsLst)
print('\n')
words.close()
wordsDoneLst = []
wordsDoneLstDuplicate = []
tempLst = []
wordsLst.sort()
for i in wordsLst:
    if i not in wordsDoneLst:
        wordsDoneLst.append(i)
    else:
        wordsDoneLstDuplicate.append(i)
        wordsLst.remove(i)
        

wordsDoneLstWithI = wordsDoneLst.copy()
for i in wordsDoneLstDuplicate:
    index = wordsDoneLst.index(i)
    if 'IIIIII' in wordsDoneLstWithI[index]:
        ''''''
    else:
        
        wordsDoneLstWithI[index] = wordsDoneLstWithI[index] + 'I'
slightlyWeak = []
decentlyWeak = []
veryWeak = []
for i in wordsDoneLstWithI:
    if 'I' in i or 'II' in i:
        slightlyWeak.append(i.replace('I',''))
    elif 'III' in i or 'IIII' in i or 'IIIII' in i:
        decentlyWeak.append(i.replace('I',''))
    elif 'IIIII' in i or 'IIIIII' in i:
        veryWeak.append(i.replace('I',''))
        
print('Slightly weak words: {}'.format(slightlyWeak))
print('Decently weak words: {}'.format(decentlyWeak))
print('Very weak words: {}'.format(veryWeak))
