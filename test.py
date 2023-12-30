import requests
import random

def get_questions(category, difficulty, limit):
    response = requests.get(f"https://opentdb.com/api.php?amount={limit}&category={category}&difficulty={difficulty}&type=multiple")
    data = response.json()
    return data["results"]

def display_questions(questions):
    for i, question in enumerate(questions, 1):
        print(f"\nQuestion {i}: {question['question']}")
        for j, option in enumerate(question['incorrect_answers'], 1):
            print(f" {j}. {option}")
        print(f" {chr(ord('A') + len(question['incorrect_answers']))}. {question['correct_answer']}")

def play_game(questions):
    score = 0
    for question in questions:
        correct_answer = question['correct_answer']
        user_answer = input(f"Enter the correct letter: ").upper()
        if user_answer == chr(ord('A') + len(question['incorrect_answers'])):
            score += 1
    return score

def main():
    category = random.randint(9, 32)
    difficulty = random.choice(["easy", "medium", "hard"])
    questions = get_questions(category, difficulty, 10)
    display_questions(questions)
    score = play_game(questions)
    print(f"\nYour final score is {score}!")

if __name__ == "__main__":
    main()