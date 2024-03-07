from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain
import random
question_bank = []
# ask = Question()
len_data = len(question_data)
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

loop = True
question = Quiz_Brain(question_bank)

while loop == True:
    question.next_question()
    question.still_has_question()  
    