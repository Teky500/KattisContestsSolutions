n = int(input()) # Input number of stacks.
InputHandle = input().split(' ')  # Input coins in each stack.
stacks = []
for value in range(n):
    stacks.append(int(InputHandle[value]))
stacksCoins = stacks
moveList = [] # Initialize moveList to be used if the answer is yes
ValidRun = True # Boolean variable to check if the run is valid.
if (sum(stacks) % 2 ) == 1:
    print('no')
    ValidRun = False # The number of coins goes down by 2 each iteration: if the number of coins is odd, the game is not possible.
else:
    # Loop until the number of coins is zero.
    # Each iteration, take away 1 coin each from the maximum and minimum stacks.
    while sum(stacksCoins) != 0:
        maxStack = max(stacksCoins)
        maxStackIndex = stacksCoins.index(maxStack) # Maximum stack and index.
        minStack = min(i for i in stacksCoins if i > 0)
        minStackIndex = stacksCoins.index(minStack) # Minimum non-zero stack and index.
        valuesAboveZero = [i for i in stacksCoins if i > 0]

        if len(valuesAboveZero) == 1:
            ValidRun = False # If there is only one value above zero, the game is impossible.
            print('no')
            break
        else:
            if maxStackIndex == minStackIndex:
                for index in range(len(stacksCoins)):
                    if (stacksCoins[index] != 0) and (index != maxStackIndex):
                        maxStackIndex = index # Making sure the indexes of maximum and minimum are distinct (when all the non-zero stacks have the same value).
        moveList.append(str(minStackIndex + 1) + ' ' + str(maxStackIndex + 1))
        stacksCoins[maxStackIndex] = maxStack - 1
        stacksCoins[minStackIndex] = minStack - 1

if ValidRun:
    print('yes')
    for i in moveList:
        print(i)