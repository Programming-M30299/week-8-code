from random import randint, random


def ten_coin_flips():
    for i in range(10):
        random_number = randint(1, 2)
        if random_number == 1:
            print("Heads")
        else:
            print("Tails")


def ten_dice_rolls():
    for i in range(10):
        dice_roll = randint(1, 6)
        print(dice_roll)


def ten_biased_coin_flips():
    heads_count = 0
    total_flips = 10
    for i in range(total_flips):
        random_number = random()
        if random_number < 0.85:
            print("Heads")
            heads_count += 1
        else:
            print("Tails")
    print(f"Heads count: {heads_count}")
    # Every time we didn't have heads, we had tails
    print(f"Tails count: {total_flips - heads_count}")
