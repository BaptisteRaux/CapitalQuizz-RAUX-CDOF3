import random

def play_game():
    print("Welcome to the Game")
    print("")
    
    try:
        number_questions = int(input("Choose the number of questions to answer: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    score = 0
    questions_list = get_questions()
    
    for i in range(number_questions):
        question, correct_answer = choose_random_question(questions_list)
        print(f"Question {i + 1}: {question}")
        
        answer = input("Your answer: ").strip().lower()
        
        if answer == correct_answer:
            print("Well answered!")
            score += 1
        else:
            print("Wrong answer.")
            print(f"The correct answer was: {correct_answer}")
        print("")

    print(f"Game over! Your final score is {score}/{number_questions}.")

def get_questions():
    return {
        "Baptiste?":"raux"

    }

def choose_random_question(questions_list):
    question = random.choice(list(questions_list.items()))
    return question[0], question[1]

def main():
    play_game()

if __name__ == "__main__":
    main()
