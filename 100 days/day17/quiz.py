from data import question_data
from question_model import Question


question_bank =[]


for questions in question_data:
    q = Question(questions["text"], questions["answer"])
    question_bank.append(q)

print(question_bank)