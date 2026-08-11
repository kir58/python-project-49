from brain_games.utils import generate_random_int

description = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(n: int) -> bool:
    return n % 2 == 0


def even_game():
    question = generate_random_int()
    answer = 'yes' if is_even(question) else 'no'
    return {'question': str(question), 'answer': answer}