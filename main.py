import random

def play_game():
    print("Welcome to the Game")
    print("")
    number_questions = int(input("Choose the number of questions to answer(max30): "))
    score = 0
    questions_list = get_questions()
    questions_answered=[]
    
    for i in range(number_questions):
        question, correct_answer = choose_random_question(questions_list,questions_answered)
        print(f"Question {i + 1}: {question}")
        
        answer = input("Your answer: ").strip().lower()

        if answer == correct_answer.lower():
            print("Well answered!")
            score += 1
        else:
            print("Wrong answer")
            print(f"The correct answer was: {correct_answer}")
        print("")
        questions_answered.append(question)

    print(f"Game over! Your final score is {score}/{number_questions}")

def get_questions():
    return {
        "Algeria":"Alger",
        "Argentina": "Buenos Aires",
        "Australia": "Canberra",
        "Brazil": "Brasilia",
        "Canada": "Ottawa",
        "Chile":"Santiago",
        "China": "Beijing",
        "Colombia": "Bogota",
        "France": "Paris",
        "Germany": "Berlin",
        "Ghana":"Accra",
        "Indonesia": "Jakarta",
        "Italy": "Rome",
        "Japan": "Tokyo",
        "Kenya": "Nairobi",
        "Mexico": "Mexico",
        "Morocco":"Rabat",
        "Nigeria":"Abuja",
        "Russia": "Moscow",
        "Spain": "Madrid",
        "Sweden": "Stockholm",
        "Thailand": "Bangkok",
        "Tunisia":"Tunis",
        "Turkey": "Ankara",
        "United Kingdom": "London",
        "United States": "Washington",

    }

def choose_random_question(questions_list,question_answered):
    while True:
        question = random.choice(list(questions_list.items()))
        if question[0] not in question_answered:
            return question[0], question[1]
    
def main():
    play_game()

if __name__ == "__main__":
    main()
