#coci18c4p1 - Elder

startingWizard = str(input())
numOfDuels = int(input())

battleSequence = ''

wandChangeCount = 1
currentWizard = startingWizard

for letter in range(numOfDuels):
    battleSequence = battleSequence + str(input())

for wizard in range(len(battleSequence)):
    if battleSequence[wizard - 1] == ' ':
        if (battleSequence[wizard] == startingWizard) and (battleSequence[wizard - 2] != startingWizard):
            if wizard == 2:
                wandChangeCount = wandChangeCount + 1
                currentWizard = battleSequence[wizard - 2]
        if (battleSequence[wizard] == currentWizard) and (battleSequence[wizard - 2] != currentWizard):
            wandChangeCount = wandChangeCount + 1
            currentWizard = battleSequence[wizard - 2]

print(currentWizard)
print(wandChangeCount)