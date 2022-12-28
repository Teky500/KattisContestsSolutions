bacteria = 1
numberExperiments = int(input())
experimentValues = input().split(' ')
experimentValueNeeded = []
for value in range(numberExperiments):
    experimentValueNeeded.append(int(experimentValues[value]))
notError = True
for experiment in range(len(experimentValueNeeded)):
    bacteria *= 2
    bacteria -= experimentValueNeeded[experiment]
    if bacteria < 0:
        print('error')
        notError = False
        break
if notError:
    print(bacteria % (10**9 + 7))