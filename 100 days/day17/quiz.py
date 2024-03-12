from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank =[]


for questions in question_data:
    q = Question(questions["text"], questions["answer"])
    question_bank.append(q)

print(question_bank)


quiz = QuizBrain(question_bank)
#quiz.next_question()


while quiz.still_has_questions():
    quiz.next_question()


print(f'your final score is : {quiz.score}/{quiz.question_no}')