loopCount = int(input())
displayLetter = 'A'

for l in range(loopCount):
    if (l == 0) and (displayLetter == 'A'):
        displayLetter = 'B'
        continue
    if (l == 1) and (displayLetter == 'B'):
        displayLetter = 'BA'
        continue
    if displayLetter[-1] == 'B':
        displayLetter = displayLetter + 'BA'
    if displayLetter[-1] == 'A':
        displayLetter = displayLetter + 'B'
    print(str(l) + str(displayLetter))

print(str(displayLetter.count('A')) + ' ' + (str(displayLetter.count('B'))))
