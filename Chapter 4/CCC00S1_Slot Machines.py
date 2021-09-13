#CCC '00 S1 - Slot Machines
# Take user input. Four inputs total. Quarters, Machine 1, Machine 2, Machine 3.
quarters = input(int())
machine1PlayedLast = input(int())
machine2PlayedLast = input(int())
machine3PlayedLast = input(int())

currentMachine = 1
playCounter = 0

# We will need to write a while loop to loop based on the number of quarters Martha has.
while quarters > 0:
    if currentMachine == 1:
        if machine1PlayedLast == 35:
            quarters = quarters + 30
            currentMachine = 2
            playCounter = playCounter + 1
        else:
            quarters = quarters - 1
            currentMachine = 2
            playCounter = playCounter + 1
    if currentMachine == 2:
        if machine2PlayedLast == 100:
            quarters = quarters + 60
            currentMachine = 3
            playCounter = playCounter + 1
        else:
            quarters = quarters - 1
            currentMachine = 3
            playCounter = playCounter + 1
    if currentMachine == 3:
        if machine3PlayedLast == 10:
            quarters = quarters + 9
            currentMachine = 1
            playCounter = playCounter + 1
        else:
            quarters = quarters - 1
            currentMachine = 1
            playCounter = playCounter + 1

print("Martha plays " + playCounter + " times before going broke.")