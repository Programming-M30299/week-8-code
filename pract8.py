from random import randint, random


def tenCoinFlips():
    for i in range(10):
        randomNumber = randint(1, 2)
        if randomNumber == 1:
            print("Heads")
        else:
            print("Tails")


def tenDiceRolls():
    for i in range(10):
        diceRoll = randint(1, 6)
        print(diceRoll)


def tenBiasedCoinFlips():
    headsCount = 0
    totalFlips = 10
    for i in range(totalFlips):
        randomNumber = random()
        if randomNumber < 0.85:
            print("Heads")
            headsCount += 1
        else:
            print("Tails")
    print("Heads count: ", headsCount)
    # Every time we didn't have heads, we had tails
    print("Tails count: ", totalFlips - headsCount)
