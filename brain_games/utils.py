import random


def is_even(n: int) -> bool:
    return n % 2 == 0


def generate_random_int(start=1, end=1000) -> int:
    return random.randint(start, end)