import json
import random

class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def display(self):
        print(self.question)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

class QuizGame:
    def __init__(self, questions):
        self.questions = [Question(**q) for q in questions]
        self.score = 0

    def play(self):
        random.shuffle(self.questions)
        for question in self.questions:
            question.display()
            user_answer = input("Your answer (enter the option number): ")
            if user_answer.isdigit() and 1 <= int(user_answer) <= len(question.options):
                selected_option = question.options[int(user_answer) - 1]
                if selected_option == question.correct_answer:
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"Wrong! The correct answer is: {question.correct_answer}\n")
            else:
                print("Invalid input. Please enter a valid option number.\n")

    def display_score(self):
        print(f"Your final score is: {self.score}/{len(self.questions)}")

def main():
    file_path = r"F:\Task Two\Day8Task\ques.json"  
    with open(file_path, "r") as file:
        questions_data = json.load(file)

    game = QuizGame(questions_data)
    game.play()
    game.display_score()

if __name__ == "__main__":
    main()
