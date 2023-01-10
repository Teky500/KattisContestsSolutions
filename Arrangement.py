# You can always split teams into a combination of a number and a number less than it by 1.
# Just find how much can be evenly divided into the number of teams by whole division, then add one team to each room until there is no remainder left.

numberOfRooms = int(input())
numberOfTeams = int(input())

smallerNumber = numberOfTeams // numberOfRooms
Buffer = numberOfTeams % numberOfRooms
Counter = Buffer

for i in range(numberOfRooms):
    for k in range(smallerNumber):
        print('*', end = '')
    if Counter > 0:
        Counter -= 1
        print('*')
    else:
        print('')
