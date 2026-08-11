from brain_games.game_flow import game_flow
from brain_games.games.brain_prime import description, prime_game


def main():
    game_flow(description, prime_game)


if __name__ == "__main__":
    main()