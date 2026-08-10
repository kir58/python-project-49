import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.utils import generate_random_int, is_even


right_answer = 3

def main():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0

    while count != right_answer:
        random_int = generate_random_int()
        print(f"Question: {random_int}")

        user_answer = prompt.string('Your answer:')
        correct_answer = 'yes' if is_even(random_int) else 'no'

        if correct_answer == user_answer:
            print("Correct!")
            count += 1

        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            break

    if count == 3:
        print(f"Congratulations, {user_name}!")