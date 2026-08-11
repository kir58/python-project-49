from brain_games.utils import generate_random_int

description = 'What number is missing in the progression?'
progression_length = 10


def progression_game():
    start_number = generate_random_int(1, 100)
    step_number = generate_random_int(1, 10)
    secrete_place = generate_random_int(0, progression_length - 1)
    progression = []

    for i in range(0, progression_length):
        if i == secrete_place:
            progression.append("..")
        else:
            progression.append(str(start_number + step_number * i))

    question = ' '.join(progression)
    answer = str(start_number + secrete_place * step_number)
    return {'question': question, 'answer': answer}




