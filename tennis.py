from random import random


def main():
    pr_win_pt, num_games = get_inputs()
    wins = simulate_n_games(pr_win_pt, num_games)
    print_summary(wins, num_games)


def get_inputs():
    pr_win_pt = float(
        input("Probability of winning a point (a float between 0 and 1): "))
    num_games = int(
        input("Number of games to simulate (a positive integer): "))
    return pr_win_pt, num_games


def simulate_n_games(pr_win_pt, num_games):
    wins = 0
    for game in range(num_games):
        points_pl, points_op = simulate_game(pr_win_pt)
        if points_pl > points_op:
            wins += 1
    return wins


def simulate_game(pr_win_pt):
    points_pl, points_op = 0, 0
    while not game_over(points_pl, points_op):
        if random() < pr_win_pt:
            points_pl += 1
        else:
            points_op += 1
    return points_pl, points_op


def game_over(points_pl, points_op):
    return (points_pl >= 4 or points_op >= 4) and abs(points_pl - points_op) >= 2


def print_summary(wins, num_games):
    print(f"Wins: {wins}")
    print(f"Total games: {num_games}")
