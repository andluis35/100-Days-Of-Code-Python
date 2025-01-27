class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score = 0

    def still_has_questions(self):
       return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}) {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right! :D")
            self.score += 1
        else:
            print("That's wrong :(")

        print(f"The correct answer was: {correct_answer}")
        self.print_partial_score()

    def print_partial_score(self):
        print(f"The current score is: {self.score}/{self.question_number + 1}")
        print("\n")

    def print_final_score(self):
        print("----------------------------------")
        print("You've completed the quiz!")
        print(f"Your final score was: {self.score}/{len(self.question_list)}")
        print("----------------------------------")
        print("\n")