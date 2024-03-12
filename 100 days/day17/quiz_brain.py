class QuizBrain:

    def __init__(self, q_list):
        self.question_no = 0
        self.question_lst = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_lst[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}{current_question.text} (True / False)")

        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return len(self.question_lst) > self.question_no

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('Youre right')
        else:
            print('Wrong')

        print(f'Current score is {self.score}/{self.question_no}.')
        print(f'Correct answer was {correct_answer}.')
