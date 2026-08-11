import math

from brain_games.utils import generate_random_int

description = 'Answer "yes" if given number is prime. Otherwise answer "no"'


def is_prime(n):
    if n < 2:
        return False
    limit = math.ceil(math.sqrt(n))
    for i in range(2, limit):
        if n % i == 0:
            return False

    return True


def prime_game():
    n = generate_random_int(1, 100)
    answer = 'yes' if is_prime(n) else 'no'
    return {'question': str(n), 'answer': answer}