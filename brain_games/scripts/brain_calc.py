from brain_games.game_flow import game_flow
from brain_games.games.brain_calc import calc_game, description


def main():
    return game_flow(description, calc_game)


if __name__ == "__main__":
    main()