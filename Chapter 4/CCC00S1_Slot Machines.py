#CCC '00 S1 - Slot Machines
# Take user input. Four inputs total. Quarters, Machine 1, Machine 2, Machine 3.
quarters = int(input())
machine1PlayedLast = int(input())
machine2PlayedLast = int(input())
machine3PlayedLast = int(input())

currentMachine = 1
playCounter = 0

# We will need to write a while loop to loop based on the number of quarters Martha has.
while quarters >= 1:
    if currentMachine == 1:
        if machine1PlayedLast == 35:
            quarters = quarters + 30
            machine1PlayedLast = 0
            playCounter = playCounter + 1
            currentMachine = 2
        else:
            quarters = quarters - 1
            playCounter = playCounter + 1
            machine1PlayedLast = machine1PlayedLast + 1
            currentMachine = 2
    elif currentMachine == 2:
        if machine2PlayedLast == 100:
            quarters = quarters + 60
            playCounter = playCounter + 1
            machine2PlayedLast = 0
            currentMachine = 3
        else:
            quarters = quarters - 1
            playCounter = playCounter + 1
            machine2PlayedLast = machine2PlayedLast + 1
            currentMachine = 3
    elif currentMachine == 3:
        if machine3PlayedLast == 10:
            quarters = quarters + 9
            playCounter = playCounter + 1
            machine3PlayedLast = 0
            currentMachine = 1
        else:
            quarters = quarters - 1
            playCounter = playCounter + 1
            machine3PlayedLast = machine3PlayedLast + 1
            currentMachine = 1

print("Martha plays " + str(playCounter) + " times before going broke.")