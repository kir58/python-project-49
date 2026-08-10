import random

def is_even(n: int) -> bool:
    return n % 2 == 0

def generate_random_int() -> int:
    return random.randint(1, 100)