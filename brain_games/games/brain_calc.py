from brain_games.utils import generate_random_int

description = 'What is the result of the expression?'


def calc_game():
    operand_1 = generate_random_int(1, 10)
    operand_2 = generate_random_int(1, 10)
    operator_key = generate_random_int(1, 3)

    answer = ''
    question = ''

    match operator_key:
        case 1:
            question = f"{operand_1} + {operand_2}"
            answer = str(operand_1 + operand_2)

        case 2:
            question = f"{operand_1} * {operand_2}"
            answer = str(operand_1 * operand_2)
        case _:
            question = f"{operand_1} - {operand_2}"
            answer = str(operand_1 - operand_2)

    return {'question': question, 'answer': str(answer)}