from brain_games.utils import generate_random_int

description = 'Find the greatest common divisor of given numbers.'

def gsd(a, b):
    if b == 0:
        return a
    return gsd(b, a % b)

def gsd_game():
    number_1 = generate_random_int()
    number_2 = generate_random_int()
    answer = gsd(number_1, number_2)
    question = f"{number_1} {number_2}"

    return { 'question': question, 'answer': str(answer) }