# Solution is based around finding two numbers: the Upper Bound and the Lower Bound
# It's necessary to find the digits that are not in the number first, and then find the front digit of the number
# The lower bound will be the number lower than the initial number,
# found by putting the maximum available digit less than the front digit of the number first and then the maximum availible digit after
# the upper bpunded will be hte number higher than the initial number,
# found by putting the minimum available digit higher than the front digit of the number first and then the minimum available digit after
# If no numbers are available to be put in the front digit for either case, either increase the length of the number by 1 or decrease it by 1
Number = input()
numberLength = len(Number)
availableNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for n in Number:
    if n in availableNumbers:
        availableNumbers.remove(n)
if len(availableNumbers) == 0:
    print('Impossible')
elif Number == '0':
    print('1')
elif Number == '1':
    print('0', '2')
else:
    topValue = Number[0]
    HigherValues = []
    LowerValues = []
    for n in availableNumbers:
        if n > topValue:
            HigherValues.append(n)
        else:
            LowerValues.append(n)
    UpperBound = ''
    LowerBound = ''
    if len(HigherValues) == 0:
        if min(LowerValues) == '0':
            if len(LowerValues) == 1:
                UpperBound = '0'
            else:
                UpperBound += LowerValues[1]
        else:
            UpperBound += LowerValues[0]
        for i in range(numberLength):
            UpperBound += min(availableNumbers)
            LowerBound += max(availableNumbers)
    elif len(LowerValues) == 0:
        for i in range(numberLength-1):
            LowerBound += max(availableNumbers)
        for i in range(numberLength):
            UpperBound += min(availableNumbers)
    elif LowerValues == ['0']:
        for i in range(numberLength-1):
            LowerBound += max(availableNumbers)
        UpperBound += min(HigherValues)
        for i in range(numberLength-1):
            UpperBound += min(availableNumbers)
    else:
        UpperBound += min(HigherValues)
        LowerBound += max(LowerValues)
        for i in range(numberLength-1):
            UpperBound += min(availableNumbers)
            LowerBound += max(availableNumbers)
    if UpperBound == LowerBound and UpperBound == '':
        print('Impossible')
    else:
        x = abs(int(UpperBound)-int(Number))
        y = abs(int(LowerBound)-int(Number))
        d = [int(LowerBound), int(UpperBound)]
        if x == y:
            if int(LowerBound) == 0 and int(UpperBound) == 0:
                print(0)
            elif int(LowerBound) == int(UpperBound):
                print(int(LowerBound))
            else:
                print(min(d), max(d))
        elif (x > y):
            print(int(LowerBound))
        elif (x < y):
            print(int(UpperBound))