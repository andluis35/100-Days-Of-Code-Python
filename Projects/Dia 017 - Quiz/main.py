from art import logo
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def fill_question_bank():
    total_questions = []
    for question in question_data:
        new_question = Question(question["text"], question["answer"])
        total_questions.append(new_question)
    return total_questions

def print_header():
    print(logo)

def start_quiz():
    print_header()
    question_bank = fill_question_bank()
    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    quiz.print_final_score()

start_quiz()
