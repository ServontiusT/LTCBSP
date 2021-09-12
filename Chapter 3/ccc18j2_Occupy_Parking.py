spots = int(input())
yesterday = input()
today = input()

spots_occupied = 0

for spot in range(len(yesterday)):
    if today[spot] == "C" and yesterday[spot] == "C":
        spots_occupied = spots_occupied + 1

print(spots_occupied)