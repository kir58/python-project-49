from brain_games.utils import generate_random_int

description = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(n: int) -> bool:
    return n % 2 == 0


def even_game():
    n = generate_random_int()
    answer = 'yes' if is_even(n) else 'no'
    return {'question': str(n), 'answer': answer}