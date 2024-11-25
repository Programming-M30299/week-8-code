# Lecture 8 - an example of top-down design
from random import random


def get_inputs():
    point_win_probability = float(input("Probability of winning each point: "))
    number_of_games = int(input("Games to simulate: "))
    return point_win_probability, number_of_games


def simulate_games(point_win_probability, number_of_games):
    wins = 0
    for game in range(number_of_games):
        points_player, points_opponent = simulate_game(point_win_probability)
        if points_player > points_opponent:
            wins = wins + 1
    return wins


def simulate_game(point_win_probability):
    points_player, points_opponent = 0, 0
    while not game_over(points_player, points_opponent):
        if random() < point_win_probability:
            points_player = points_player + 1
        else:
            points_opponent = points_opponent + 1
    return points_player, points_opponent


def game_over(points_player, points_opponent):
    return (points_player >= 4 or points_opponent >= 4) and \
        abs(points_player - points_opponent) >= 2


def print_summary(wins, number_of_games):
    proportion = wins / number_of_games
    print(f"Wins: {wins}, proportion: {proportion:.2f}")


def main():
    point_win_probability, number_of_games = get_inputs()
    wins = simulate_games(point_win_probability, number_of_games)
    print_summary(wins, number_of_games)
