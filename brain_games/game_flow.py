import prompt

steps = 3


def game_flow(description: str, get_answer_question) -> None:
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(description)

    for i in range(steps):
        data = get_answer_question()
        answer = data['answer']
        question = data['question']

        print(f'Question: {question}')

        user_answer = prompt.string('Your answer:')

        if answer == user_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{answer}'.")
            print(f"Let's try again, {user_name}!")
            return

    print(f"Congratulations, {user_name}!")
