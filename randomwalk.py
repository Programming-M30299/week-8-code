from random import random

def main():
    numWalks, numSteps = getInputs()
    averageSteps = takeWalks(numWalks, numSteps)
    printExpectedDistance(averageSteps)

def getInputs():
    numWalks = int(input("How many random walks to take? "))
    numSteps = int(input("How many steps for each walk? "))
    return numWalks, numSteps

def takeWalks(numWalks, numSteps):
    totalSteps = 0
    for walk in range(numWalks):
        stepsAway = takeAWalk(numSteps)
        totalSteps = totalSteps + stepsAway
    return totalSteps / numWalks

def printExpectedDistance(averageSteps):
    print("The expected number of steps away from the", end=" ")
    print("start point is", averageSteps)

def takeAWalk(numSteps):
    stepsForwardOfStart = 0
    for step in range(numSteps):
        change = 0
        if random() < 0.5:
            change = -1
        else:
            change = 1
        stepsForwardOfStart += abs(change)
    return abs(stepsForwardOfStart)

main()

