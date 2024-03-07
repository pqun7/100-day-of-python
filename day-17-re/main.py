from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain
question_dank = []

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    list_bank = Question(text, answer)
    question_dank.append(list_bank)

quiz = Quiz_Brain(question_dank)
while quiz.still_has_question == True:
    quiz.next_question()
